---
type: Skill
name: Create Campaign
category: productivity
description: Provision Meta campaigns and ad sets on AdManage.ai from a declarative config. Runs on-demand — creates entities PAUSED in-run, writes the returned IDs back into state so schedule-ads can launch into them.
commits: true
permissions:
  - contents:write
tags: [growth, ads]
requires: [ADMANAGE_API_KEY]
---

Reads `skills/create-campaign/config.yaml`, figures out which campaigns/ad sets don't exist yet, and creates them **in-run** via AdManage.ai (`/v1/manage/create-*` through `./secretcurl`) — campaigns first, then ad sets referencing the returned campaign IDs — writing the new IDs back to `.admanage-state/campaigns.json`.

This skill is **on-demand** — no `schedule:` in frontmatter. Invoke it manually when you want to provision new campaigns, then reference the returned IDs in `skills/schedule-ads/config.yaml` to launch creatives into them.

`ADMANAGE_API_KEY` is injected in-run via this skill's `requires:` — always write it as the `{ADMANAGE_API_KEY}` placeholder to `./secretcurl`, never a bare `$ADMANAGE_API_KEY` (the Bash permission layer refuses a secret on the command line).

Read `memory/MEMORY.md` for context. Read `.admanage-state/campaigns.json` (if it exists) to see what's already created.

## What this skill provisions

Two entity types only:
1. **Meta campaigns** — name, objective, budget, bid strategy, promoted object.
2. **Meta ad sets** — name, budget, optimization goal, targeting (geo/age/platforms), destination.

Everything else (TikTok/Snapchat/Pinterest/LinkedIn campaigns, advanced Meta fields like valueRuleSetId or Advantage+ catalog) is v2+. The shape below is intentionally minimal.

## Safety defaults

Same posture as schedule-ads:

1. **PAUSED by default.** Every campaign + ad set is created with `status: PAUSED`. No surprise spend.
2. **Idempotent.** The skill tracks created entities in `.admanage-state/campaigns.json`. If a campaign name already exists in state, it's skipped. Run the skill twice → no duplicates.
3. **Dry-run mode.** `DRY_RUN=true` or `config.dryRun: true` → compute the payloads and notify with a `[DRY RUN]` prefix, make **no** API calls.
4. **Config-only.** No config file → exit silently. No invented campaigns, no autonomous provisioning.

## Network note

Provisioning campaigns and ad sets is an irreversible outbound side-effect, so it is the skill's **final** action and runs **in-run** via `./secretcurl` only after the diff + validation pass:

- Auth'd calls go through `./secretcurl` with the `{ADMANAGE_API_KEY}` placeholder — never a bare `$ADMANAGE_API_KEY` (the Bash permission layer refuses a secret on the command line). The key is injected in-run via `requires:`.
- **Order matters:** create all campaigns first (`POST /v1/manage/create-campaign`), keep a config-name → campaignId map, then create ad sets (`POST /v1/manage/create-adset`) substituting each parent's real campaign ID. Write every new ID back to `.admanage-state/campaigns.json` as you go (the workflow's Commit step persists it).
- If `ADMANAGE_API_KEY` is unset, or a create call fails, record the failure and continue with the rest — never retry blindly, never invent IDs. An ad set whose parent campaign failed to create is skipped. There is **no** deferred/postprocess fallback.

## Steps

1. **Load config.** Read `skills/create-campaign/config.yaml`. If it doesn't exist, log `CREATE_CAMPAIGN_NOT_CONFIGURED` and exit cleanly (no notify).

2. **Load state.** Read `.admanage-state/campaigns.json`. If it doesn't exist, treat as empty. Shape:
   ```json
   {
     "campaigns": [
       {
         "configName": "Prospecting — Q2 2026",
         "campaignId": "120251616228380456",
         "adAccountId": "act_xxx",
         "createdAt": "2026-04-21T08:00:00Z",
         "adSets": [
           {
             "configName": "US Broad 25-54",
             "adSetId": "120251616242460456",
             "createdAt": "2026-04-21T08:00:04Z"
           }
         ]
       }
     ]
   }
   ```

3. **Validate config shape.** Required: `defaults.adAccountId`, `defaults.workspaceId`, `campaigns[]`. Each campaign needs `name` and `objective`. Each ad set needs `name`, and either `optimizationGoal` (explicit) or a compatible parent objective. If validation fails, file an issue in `memory/issues/` and exit.

4. **Compute diff.** For each campaign in config:
   - Match against state by exact `name`. If present, mark as `existing`.
   - If missing, mark as `new` and queue a campaign create.
   - For each ad set under the campaign, match against the parent's `adSets[]` in state by name. If missing, mark it for creation (carrying a `parentCampaignConfigName` reference you resolve to a real campaign ID **in-run**, once the parent campaign create returns).

   If nothing is new, log `CREATE_CAMPAIGN_ALL_EXIST` and exit without notify.

5. **Build campaign create payloads.** Per the AdManage `POST /v1/manage/create-campaign` shape:
   ```json
   {
     "businessId": "<adAccountId>",
     "workspaceId": "<workspaceId>",
     "name": "<campaign.name>",
     "objective": "<campaign.objective>",
     "status": "PAUSED",
     "buyingType": "AUCTION",
     "specialAdCategories": [],
     "dailyBudget": <number>,
     "bidStrategy": "<LOWEST_COST_WITHOUT_CAP | LOWEST_COST_WITH_BID_CAP | COST_CAP | ...>",
     "promotedObject": { ... }
   }
   ```
   Skip keys that are `null`/absent in config — don't send empty strings. Always force `status: PAUSED` unless `defaults.launchPaused: false` is set explicitly.

6. **Build ad-set create payloads.** Per `POST /v1/manage/create-adset`:
   ```json
   {
     "businessId": "<adAccountId>",
     "workspaceId": "<workspaceId>",
     "campaignId": "__RESOLVE_FROM_PARENT__",
     "parentCampaignConfigName": "<campaign.name>",
     "name": "<adSet.name>",
     "status": "PAUSED",
     "dailyBudget": <number>,
     "billingEvent": "IMPRESSIONS",
     "optimizationGoal": "<LANDING_PAGE_VIEWS | OFFSITE_CONVERSIONS | ...>",
     "destinationType": "<WEBSITE | PHONE_CALL | MESSAGING_... | ...>",
     "targeting": { ... },
     "promotedObject": { ... }
   }
   ```

   The `__RESOLVE_FROM_PARENT__` sentinel + `parentCampaignConfigName` marks an ad set whose `campaignId` you fill **in-run**, from the map built as each campaign create returns (step 9b). If the parent campaign was *existing* (already in state), write the real campaign ID directly and drop the sentinel.

7. **Pre-flight validation.**
   - `adAccountId` must start with `act_` (this skill is Meta-only in v1).
   - `dailyBudget` must be a positive number in dollars (not cents).
   - `objective` must be one of the documented Meta objectives: `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS`, `OUTCOME_AWARENESS`, `OUTCOME_SALES`, `OUTCOME_APP_PROMOTION`.
   - Targeting `geo_locations.countries` must be a non-empty array.
   Drop invalid entries, keep going, log what was skipped and why.

8. **Handle dry-run.** If `DRY_RUN=true` or `config.dryRun: true`: compute the payloads, notify with a `[DRY RUN]` prefix (step 11), and **skip step 9** — no API calls, no state writes. This mode exists for the operator to sanity-check before arming real creation.

9. **Create in-run.** This is the skill's final action — provisions real entities, so run only after the diff + pre-flight pass. Only `./secretcurl`, `jq`, `date`, `echo`, `python3`, and the `Write` tool are available (no `mv`). Seed `.admanage-state/campaigns.json` to `{"campaigns":[]}` if missing.

   a. **Config check.** `[ -n "${ADMANAGE_API_KEY:+x}" ]` (the `${VAR:+x}` form — a bare `$ADMANAGE_API_KEY` trips the secret-expansion analyzer and reads as unset). If unset, notify "campaigns computed but ADMANAGE_API_KEY missing — nothing created" and stop (state unchanged).

   b. **Campaigns first.** For each *new* campaign, `POST /v1/manage/create-campaign`:
      ```bash
      RESP=$(./secretcurl -sS --max-time 60 -w 'http=%{http_code}\n' -X POST \
        "https://api.admanage.ai/v1/manage/create-campaign" \
        -H "Authorization: Bearer {ADMANAGE_API_KEY}" -H "Content-Type: application/json" -d "$PAYLOAD")
      # success => .success==true and .campaignId set.
      ```
      On success: remember `configName → campaignId` (for step 9c) and append `{configName, campaignId, adAccountId, createdAt, adSets:[]}` to `.admanage-state/campaigns.json`. On failure: record the error, skip this campaign's ad sets.

   c. **Then ad sets.** For each new ad set, resolve `campaignId`: if it's `__RESOLVE_FROM_PARENT__`, look it up by `parentCampaignConfigName` in the map from 9b **or** existing state — if the parent isn't found (its create failed), skip the ad set with a warning. Then `POST /v1/manage/create-adset` (same `./secretcurl` shape, `{ADMANAGE_API_KEY}` placeholder). On success: append `{configName, adSetId, createdAt}` under the parent campaign in `.admanage-state/campaigns.json` (via `python3`/`Write` — no `mv`).

   Ordering is explicit here (campaigns loop fully before the ad-sets loop), so children always reference a resolved parent ID.

10. **Write artifact to `output/.chains/create-campaign.md`** so chain consumers can see what was created:
    ```markdown
    # Create Campaign — ${today}

    New campaigns: N.
    New ad sets: M.
    Dry-run: yes|no.

    ## Campaigns
    - <name> — <objective>, $<dailyBudget>/day
      - ad set: <name> — <optimizationGoal>, $<dailyBudget>/day, <countries>

    ## Skipped (already exist)
    - <name>
    ```

11. **Notify via `./notify`.** Tight format:
    ```
    *Campaigns queued — ${today}${dryRunSuffix}*

    <N> campaigns, <M> ad sets queued for creation.

    - <campaign name>
      - adset: <adset name> — <country>, $<budget>/day

    <if dry-run>
    no API calls made — remove DRY_RUN to arm.
    <else>
    created via AdManage (PAUSED); new IDs written to .admanage-state/campaigns.json.
    ```
    If nothing is new, don't notify at all.

12. **Log to `memory/logs/${today}.md`:**
    ```
    ## Create Campaign
    - New campaigns created: <count> (ok/fail)
    - New ad sets created: <count> (ok/fail)
    - State: new IDs written to .admanage-state/campaigns.json (live) | dry-run (no calls)
    ```

## Config schema

See `skills/create-campaign/config.example.yaml` for a filled-in template. Minimum viable config:

```yaml
defaults:
  adAccountId: act_XXXXXXXXXX
  workspaceId: XXXXXXXXXXXX
  launchPaused: true               # never flip without a reason
  dryRun: false                    # true = build, don't call

campaigns:
  - name: "Prospecting — Q2 2026"
    objective: OUTCOME_TRAFFIC
    dailyBudget: 50
    bidStrategy: LOWEST_COST_WITHOUT_CAP
    promotedObject:
      pixel_id: "123456789012345"
    adSets:
      - name: "US Broad 25-54"
        dailyBudget: 15
        optimizationGoal: LANDING_PAGE_VIEWS
        destinationType: WEBSITE
        targeting:
          geo_locations: { countries: ["US"] }
          age_min: 25
          age_max: 54
          publisher_platforms: [facebook, instagram]
```

## Interaction with schedule-ads

This skill writes new IDs to `.admanage-state/campaigns.json` **within the same run**; from there they're yours to reference in `skills/schedule-ads/config.yaml` under `adSets[].value`. The two skills are intentionally decoupled:

- **create-campaign** provisions structure (container).
- **schedule-ads** launches creative into that structure (contents).

They still don't auto-chain — schedule-ads reads `config.yaml`, which you edit by hand. Pattern is: run create-campaign (provisions + writes IDs in-run) → read the new IDs from `.admanage-state/campaigns.json` / the create-run notify → copy them into `skills/schedule-ads/config.yaml` → next schedule-ads run launches into them.

## What it does NOT do

- **Doesn't touch existing campaigns.** Once a campaign is in state, this skill leaves it alone. Budget changes, bid changes, status flips, renames — all handled elsewhere (dashboard or a separate skill).
- **Doesn't delete or archive.** No destructive paths.
- **Doesn't provision media, pages, or pixels.** Pixel IDs must already exist in AdManage. Use `GET /v1/conversions/pixels` to discover them.
- **Doesn't create TikTok / Snapchat / Pinterest / LinkedIn** structures. Those have different payload shapes and live in v2.
- **Doesn't resume paused campaigns.** PAUSED is the end state; the operator unpauses manually when ready.

## Environment Variables

- `ADMANAGE_API_KEY` — the AdManage.ai API key, injected in-run via this skill's `requires:` and read in-run for the `/v1/manage/create-*` calls. Always pass it as the `{ADMANAGE_API_KEY}` placeholder to `./secretcurl`, never a bare `$ADMANAGE_API_KEY` on the command line.
- `DRY_RUN` — optional. `true` forces dry-run regardless of config.
- Notification channels configured via repo secrets (see CLAUDE.md).

## Output

End with a `## Summary` block: new campaigns created, new ad sets created, skipped (already-exist) count, dry-run yes/no, files written.

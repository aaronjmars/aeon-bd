*fetch-tweets has been dead 2 days* — it's enabled but has no `var`, so prefetch skips it and every run no-ops (no query to search). it feeds bd-radar's X path, so it's worth fixing.

pushed the one-line fix to branch `fix/fetch-tweets-set-var` (sets var to `@aeonframework OR aaronjmars/aeon OR @miroshark_ OR Miroshark swarm simulation`). can't open the PR from the runner — org blocks Actions from creating PRs — so it needs a manual merge.

*decide:* merge it, or kill fetch-tweets entirely since product-pulse + bd-radar already cover product X-deltas.

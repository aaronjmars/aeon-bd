for line in open('.replen.txt'):
    line = line.rstrip('\n')
    if not line:
        continue
    i, t = line.split('|', 1)
    print(i, 'len=', len(t))

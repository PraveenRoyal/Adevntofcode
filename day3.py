with open('input3again', 'r') as para:
    Grid = para.read().splitlines()
    total = 0
    for r, row in enumerate(Grid):
        for c, column in enumerate(row):
            if column != '*':
                continue
            cs = set()
            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if cr < 0 or cr >= len(Grid) or cc < 0 or cc >= len(Grid[cr]) or not Grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and Grid[cr][cc-1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))
            if len(cs) != 2:
                continue
            ns = []
            for lm, mn in cs:
                s = ""
                while mn < len(Grid[lm]) and Grid[lm][mn].isdigit():
                    s += Grid[lm][mn]
                    mn += 1
                ns.append(int(s))
            total += ns[0] * ns[1]
    print(total)


marks = {}
with  open(r"e:\classroom\python\nov22\demo\marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip("\n").split(",")
        if len(parts) < 2:
            continue

        # print(parts)
        name = parts[0]  # First element is name
        total = 0
        for m in parts[1:]:
            try:
                total += int(m)
            except:
                pass

                # add entry to dict
        marks[name] = total

for n, t in sorted(marks.items()):
    print(f"{n:20s} {t:3d}")

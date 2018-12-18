filename = "names.txt"

with open(filename, 'rt') as f:
    lines = f.readlines()

with open(filename, 'wt') as f:
    f.writelines(filter(lambda l: len(l) > 1, lines))

print("Done!")

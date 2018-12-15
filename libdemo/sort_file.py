
filename = "names.txt"

with open(filename,'rt') as f:
     lines = f.readlines()


with open(filename,'wt') as f:
     f.writelines(sorted(lines))

print("Done!")

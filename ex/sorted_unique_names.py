names = []

while True:
    name = input("Enter name [end to stop]: ")
    if name == "end":
        break

    if name not in names:
        names.append(name)

for n in sorted(names):
    print(n, len(n))

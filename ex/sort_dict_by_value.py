d = {10: "Abc", 20: 'Def', 15: "Pqr"}

for t in sorted(d.items(), key=lambda t: t[1]):
    print(t)

st = "Java Programming"

for c in filter(lambda ch: ch.isupper(), st):
    print(c)

for c in filter(str.islower, st):
    print(c)

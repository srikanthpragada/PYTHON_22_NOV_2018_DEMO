# Take name and mobile and print all in sorted by name

customers = {}

entries = ("Mark,3939439433","Bill,3939393933", "Larry,1919191911", "Andy,393939111")

for e in entries:
    parts = e.split(",")
    customers[parts[0]] = parts[1]

for n, m in sorted(customers.items()):
    print(f"{n:20s} {m}")

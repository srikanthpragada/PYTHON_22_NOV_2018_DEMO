names = ['R', 'Java', 'Python', 'Ruby', 'TypeScript', 'c', 'c++', 'Pascal']

def get_length(s):
    return len(s)

# for n in sorted(names, key=get_length):
#     print(n)


# for n in sorted(names, key=len):
#     print(n)

for n in sorted(names, key= lambda n : n.lower()):
    print(n)


for n in sorted(names, key = str.lower, reverse=True):
    print(n)

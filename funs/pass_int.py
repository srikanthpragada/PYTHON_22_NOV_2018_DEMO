def fun(n):
    print(id(n), n)
    n = 0

def add(lst,v):
    lst.append(v)

a = 100
print(id(a), a)
fun(a)
print(a)

l = [10,20]
add(l,30)
print(l)



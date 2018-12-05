def fun():
    print("First fun()")


def fun(n1):
    print("Second fun(n1)")


print(id(fun), type(fun))
print(fun)

fun()
fun(10)

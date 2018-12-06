g = 1  # global variable


def fun1():
    v1 = 10
    global g
    g = 1000
    # Local function
    def fun2():
        v2 = 20
        nonlocal v1
        v1 = v1 + 1
        print(v2, v1, g)

    fun2()
    print(v1)


fun1()
print(g)


def fun():
    print("In fun()")


def add(a, b=0):
    return a + b


def fun2(*, n1=1, n2):  # keyword only arguments
    pass


def fun3(*names, msg="Hello"):
    for n in names:
        print(msg, n)


def fun4(a=10, *b):
    print(a)
    print(b)


def kwargs(n1, n2, *args):
    print(n1,n2)
    print(args)


kwargs(10,20)

# fun3("abc", 'pqr', msg="Good Evening")
# fun4(10,20,30)

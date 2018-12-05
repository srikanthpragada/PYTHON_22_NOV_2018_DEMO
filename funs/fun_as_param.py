def operation(n1, n2, task):
    return task(n1, n2)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(operation(10, 20, add))
print(operation(10, 20, mul))

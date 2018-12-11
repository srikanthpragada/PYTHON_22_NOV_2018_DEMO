class A:
    def print(self):
        print("In print of A")

    def process(self):
        print("In Process of A")


class B:
    def print(self):
        print("In print of B")


class C(B, A):
    pass


obj = C()
obj.print()
obj.process()

print( isinstance(obj,C))
print( isinstance(10,int))
print( issubclass(int,object))


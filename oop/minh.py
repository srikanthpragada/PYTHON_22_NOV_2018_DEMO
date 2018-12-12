class Common:
    def print(self):
        print("In print of Common")


class A(Common):
    # def print(self):
    #     print("In print of A")

    def process(self):
        print("In Process of A")


class B(Common):
    def print(self):
        print("In print of B")


class C(A):
    pass


obj = C()
# obj.print()
print(C.mro())


class  MyNumbers:
    def __init__(self):
        self.nums = [10,20,30]

    def __iter__(self):
        self.pos = 0
        return  self

    def __next__(self):
       if self.pos < len(self.nums):
           v =  self.nums[self.pos]
           self.pos += 1
           return v
       else:
           raise StopIteration


def my_numbers():
    for n in range(1,6):
        yield  n

def squares(n):
    for v in range(1,n+1):
        yield  v*v

for v in squares(10):
    print(v)



# n = MyNumbers()
# i = iter(n)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# for v in n:
#     print(v)



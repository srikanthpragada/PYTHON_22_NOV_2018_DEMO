
nums = [10, 20, 11, 22, 33, 55]
names = ['c','c++','Java','Python']

odd_nums = filter(lambda n : n % 2 == 1, nums)

for n in odd_nums:
    print(n)

for n in filter(lambda v : len(v) > 3, names) :
    print(n)


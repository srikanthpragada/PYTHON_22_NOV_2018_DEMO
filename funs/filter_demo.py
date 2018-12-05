def is_odd(n):
    print(n)
    return n % 2 == 1


nums = [10, 20, 11, 22, 33, 55]

odd_nums = filter(is_odd, nums)

for n in odd_nums:
    print(n)

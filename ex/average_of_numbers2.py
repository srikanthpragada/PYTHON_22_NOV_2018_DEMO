total = 0
count = 0

while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break
        total += num
        count += 1
    except:
        print("Invalid number!")


print("Average = ", total / count)






filename = "test.txt"

chars = words = lines = 0

with open(filename,'rt') as f:
    for l in f:
        lines +=1
        chars += len(l)
        if len(l) > 1:  # Ignore blank line
            parts = l.strip('\n').split(" ")
            print(parts)
            words += len(parts)


print(f"Chars = {chars}, Words = {words}, Lines ={lines}")



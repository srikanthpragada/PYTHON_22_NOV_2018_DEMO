class AmountError(Exception):
    def __init__(self,message):
       self.message = message

try:
    num = int(input("Enter number :"))
    print(100 / num)
    raise AmountError("Abc...")
except ValueError:
    print("Invalid input")
except Exception as ex:
    print("Some other error -->", str(ex))
else:
    print("Done")
finally:
    print("The End!")

print("Continue....")





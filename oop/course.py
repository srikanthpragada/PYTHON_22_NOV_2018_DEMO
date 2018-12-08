class Course:
    # Constructor
    def __init__(self, name, duration=None, f=None):
        # Object attributes
        self.name = name
        self.__duration = duration
        self.__fee = f

    def __str__(self):
        return  f"{self.name} - {self.__duration} - {self.__fee}"


c1 = Course("Python", 40, 4000)   # Create object
print(str(c1))  # c1.__str__()
# print(c1.name,c1.__duration)


c2 = Course("Data Science", f=10000)
print(c2)




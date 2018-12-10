class Course:
    # Class attributes
    taxper = 15

    @staticmethod
    def change_taxper(newtaxper):
        Course.taxper = newtaxper

    # Constructor
    def __init__(self, name, duration=None, f=None):
        # Object attributes
        self.name = name
        self.duration = duration
        self.fee = f

    def get_fee(self):
        return  self.fee + self.fee * Course.taxper / 100

    # Special method
    def __str__(self):
        return  f"{self.name} - {self.duration} - {self.fee}"

    def __eq__(self,other):
        print("__eq__")
        return self.name == other.name and self.duration == other.duration  and self.fee == other.fee

    def __gt__(self, other):
        return self.fee > other.fee


c1 = Course("Python", 40,4000)   # Create object
Course.change_taxper(20)
print(c1.get_fee())













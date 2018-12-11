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

    @property
    def netfee(self):
        return self.fee + self.fee * Course.taxper / 100

    # Special method
    def __str__(self):
        return f"{self.name} - {self.duration} - {self.fee}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.duration == other.duration and self.fee == other.fee

    def __gt__(self, other):
        return self.fee > other.fee


class OnlineCourse(Course):
    def __init__(self, weburl, name, duration=None, fee=None):
        # super().__init__(name,duration,fee)
        Course.__init__(self, name, duration, fee)
        self.weburl = weburl


c1 = Course("Python", 40, 4000)  # Create object
c2 = OnlineCourse("http://wbxy", "Angular")
print(c2.name)
print(OnlineCourse.__bases__)

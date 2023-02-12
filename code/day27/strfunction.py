class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name is {self.name} and age is {self.age}"
a=Student("ram",22)
print(a)
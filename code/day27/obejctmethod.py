class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def showdata(self):               #here showdata() is a method of objects(i.e function)
        print(f"Employee name {self.name} age is {self.age} and salary is {self.salary}")
s=Employee("ram",45,10000)
s.showdata()
#Output: Employee name ram age is 45 and salary is 10000
# modifying object
s.age=50
s.showdata()
#ouput:Employee name ram age is 50 and salary is 10000
#deleting object
del s.age
s.showdata()
#error due to missing attributes

#we cannot create empty class if we dont have content we simply put pass
class Hero:
    pass
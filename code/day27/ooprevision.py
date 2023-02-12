class Student:                             #creating a class 
    def __init__(self,name,age):           #init function 
        self.name=name
        self.age=age
    def showdata(self):                        #function to display data
        print("Studnet name is",self.name)
        print("Student age is",self.age)
a=Student("ram",22)                            #passing parameters to init function
a.showdata()                                   #showdata function get called and print output
print(str(a))
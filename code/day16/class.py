class employee:                      #class class_name
    def __init__(self):              #def method (variable)
        self.name="ram"              #properties or variable
        self.address="Kathmandu"
        self.salary="20k"
    def talk(self):                  # def method
        print("Hello I am ",self.name)
        print("I live in ",self.address)
        print("I am earning",self.salary)
e=employee()                         # reference variable = object
print(e.name)
e.talk()
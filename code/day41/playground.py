class Student:
    def __init__(self, **kw):
        self.name = kw["name"]
        self.add = kw["add"]


st = Student( name = "ram" , add = "nepal")
print(st.name)


#these program show ValyeError if entered data is string show we can handle it by try and expect
try:
    number=int(input("Enter number whose multiplication is to be calculated : "))

    for i in range(0,11):
     print(f"{number} X {i} = {number*i}")
except ValueError:
    print("Error has occured ")
print("The code that is not affected by error ")
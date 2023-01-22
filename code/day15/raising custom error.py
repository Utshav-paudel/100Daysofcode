# raising error example
number=int(input("Enter any number between 1-4"))
# here if we want to raise error if user give value not between 1-4
if number<1 or number>4:
    raise ValueError("enter number only between 1-4")
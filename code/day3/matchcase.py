x=int(input("Enter any option below :"))
match x:
    case 1:
        print("This is 1")
    case 2:
        print("This is 2")
    case 3:
        print("This is 3")
    case 4:
        print("This is 4")
    case _:
        print("This is user input",x)
    
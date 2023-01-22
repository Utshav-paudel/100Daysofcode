# create a dcitionary 
employee={"ram":129000,"alex":46666,"antony":12999,"ramesh":20000}
#if we have to remove any key value pair then use pop()
employee.pop("antony")   #antony left so we are removing his data
print(employee)
#{'ram': 129000, 'alex': 46666, 'ramesh': 20000} 

#del method is used to delete dictionary
del employee
print(employee)   #error occured since employee is deleted

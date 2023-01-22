#lets create one dictionaries of employee salary 
employee={"ram":10000,"shyam":15999,"hari":12000,"gita":12500}
#we have another dictionaries of addition employee
employeeadded={"ramesh":12000,"ramparsad":34994,"alex":34358}

#lets create one dictionary by updating data of second dictionary in first
#by using update() fucntion
employee.update(employeeadded)
print(employee)

#{'ram': 10000, 'shyam': 15999, 'hari': 12000, 'gita': 12500, 'ramesh': 12000, 'ramparsad': 34994, 'alex': 34358} will be prinetd as output
dict1={234:12,235:89,238:23}
dict2={234:17,239:45}
dict1.update(dict2)
print(dict1)
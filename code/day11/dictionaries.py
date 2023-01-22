info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())
#output:
#{'name': 'Karan', 'age': 19, 'eligible': True}
# dict_keys(['name', 'age', 'eligible'])
# dict_values(['Karan', 19, True]) 

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  
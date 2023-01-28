day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# here enumerate function will display value and index in tuple
for days in enumerate(day):
    print(days)

# using index will unpack the tuple
day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for index,days in enumerate(day):
    print(index,days)

# also we can set the starting index
# indexing start from 1 in this code below
day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for index,days in enumerate(day,start=1):
    print(index,days)
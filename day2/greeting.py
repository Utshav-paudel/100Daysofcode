import time
print(time)
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hrs = int(time.strftime('%H'))
print(timestamp)
min = int(time.strftime('%M'))
print(timestamp)
sec = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
if(hrs<=12):
    print("Good morning")
elif(hrs<=22):
    print("Good afternoon")
else:
    print("Good night")
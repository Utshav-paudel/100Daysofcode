# 100Daysofcode
#Welcome to my journey of 100 days of coding 
##Everyday I will be updating what I learn that day here.

# Day 1
<p>Today I learned some basics in python like data types in python and about typecasting in python.
There are two types of typecasting in python </P>
1.Implicit typecasting
  conversion data types by program itself for e.g: 
  
```
  a=10
     b=2.0
     sum=a+b
     print(sum)
     #sum will be in float because of implicit typecasting
   
 ```
 
2. Explicit typecasting
  
<p>conversion of data types by programmer is called explicit typecasting .
  for e.g :</p>
  <break>
  
 ```
  a=10
     b=2
     sum=a+b
     print(float(sum))
     #sum is in integer and changed to float using explicit typecasting
 
  ```

# Day 1 project Calculator :
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/c3f966a86f9b31b7ab15ca3c510dfb08c7e142f8/images/day1.png)

# Day 2 
  
<p>Here in day 2 of codes I have learned about string slicing . String in python is similar to array .
  </p>

```
  
 name="Elephant"
 length=len(name) #this len function provides the length of name
 print(name[2:3]) #this print e
 print(name[1:5]) #this print leph
 #this above example is string slicing
  ```
  
# Greeting program
  <p>This program greet you according to your time .
    It import time from your computer using 
    
import time
    
#Then it convert time into string using
 
strftime()
    
    
After that greeting is done using elif codition as seen below :
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/93fbbe9995de8412ee7ee40ad2198a4bae846e40/images/day2.png)
    
# Day3
    
### Match case statement 
    
 Match case is similar to switch case in c and c++ but there is no necesary of using break
    If you donot know about c and c++
    Match case is used to select case according to option here is a sample program:
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/5c6c149cad4c4ad67ca330a028c828d6187dce79/images/day3.png)
    
# Day4
### List
   
Is sequence data types in python that is a collection of sequence elements 
for e.g:
    
`lst=[1,2,56,"hari","alex",false]`
    
 Yes as you can see list can contains different data types.
    
 Tuples is also similar to list but it cannot be changed (i.e immutable)
 Clear explanation of list is shown below
 ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/59128304cd86677286b6edf1c348fc0c3353813f/images/day4.png)

 ### List method
  There are various method to perform with list that help in program some of them are:
  
  #### list.sort()
    
It sort the list in ascending order
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/245832c2f68774d3a609da722b8b3992e3782a63/images/day4.1.png)
    
#### list.index()
     
It gives index of frist occurence of the list item
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/c47288693ca44e444e6a927b8bb489792378db55/images/day4.2.png)
    
here output will be 1 for colours list and 3 for num list .
    
#### list.count
    
It counts number the number of items of given value 
for e.g `colors.count("green")`
This will count number of time green occured in list colors 
    
All others important list method are as follows :

  ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/e2ec5aea55ef65ef785927616f4c51ebaf665b98/images/day4.3.png)
    
  ![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/e2ec5aea55ef65ef785927616f4c51ebaf665b98/images/day4.4.png)
    
# Day5
   
Today we are going to learn about the tuples in python . Tuples are similar to list but it is immutable(i.e it cannot be changed).
It also hold collection of data items . Tuples items are separated with comma and enclosed with small brackets for e.g:

    tuple=(1,4,6,7)
    tuple=(1)
    print(type(tuple))  #this is printed as class int it should contain one , to be tuple
    tuple=(1,)           
    print(type(tuple))  #this is printed as class tuple
    
##### Note : Tuples cannot be changed it is constant and use in cases where we want constant list .
![alt enter](https://github.com/Peterpaudel/100Daysofcode/blob/4584edefb0d8a4ca56495ed1b7d8b17480db45b3/images/day5.png)

# Day6
Today I learned about the method on tuples . Tuples exactly is immutable so it does not have any method that changes data item but we can perform this by changing tuples into list changing data items and changing it to tuples . Although we can perform some operation like index,len,etc .
Code for the method in tuples is shared below hope you get some insights .

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/80dff58495fd5b62d44aa44661f10ce792b65148/images/day6.png)
    
# Day7
### f-string
 f-string is a new string formatting mechanism that allow us to enter variable directly in between the string according to our format.
 for e.g:
 
    val="geek"
    print(f"{val} for {val} is a portal for {val}")
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/cb31e2c50667345c4ed21c81453d9659086e7548/images/day7.png)

 

# Update coming tomorrow

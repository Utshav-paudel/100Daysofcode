# 100Daysofcode
### Welcome to my journey of 100 days of coding 
### Everyday I will be updating what I learn that day here.

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
    
### Docstrings
Python docstrings are the string literals that appears right after the definition of function,class,method or module.
Its like comment but its not ignored by python interpreter and cannot be used anywhere it mostly used to describe function workflow

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/bef684dc84d366f49f1c137c537b9c9bec0f87ca/images/day7.png)
    
### PEP 8
PEP 8 is a guidline in python programming that makes python readable,maintainable and consistent . It stands for Python Enhancement Proposals
    
### Set
Set is an unordered collection of data items in a single variable enclosed by curly braces and element separated by comma . Set doesnot contain duplicate item 
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/dc5121c0f0733c8c27e2a5e4082100236f090538/images/day7.2.png)
    
# Day8
### Recursion
Recursion is the special case in which function call itself directly or indirectly to meet desired result.
such function is called recursive function 

![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/f93fd737e715a8762c40d780a707fc772fc9423d/images/day8.png)
    
# Day9
### Methods on sets
#### 1.union() and update()
  union() helps to find the union of two sets and update helps to update the sets value.
    
    s1={1,4,5,7,9}
    s2={1,4,6,7,8,9}
    print(s1.union(s2))
    s1.update(s2)
    print(s1)
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/94caa59a9b69ec41fc31f6b36c5f3784140367b8/images/day9(union%20and%20update).png)
#### 2.intersection() and intersection_update()
  intersection() finds common value of two sets wherease intersection_update() update the sets with intersection.
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/94caa59a9b69ec41fc31f6b36c5f3784140367b8/images/day9(difference%20and%20difference_update).png)
#### 3.symmetric_difference() and symmetric_difference_update()
  symmetric_difference() gets items that are not similar on two sets and symmetric_difference_update() the sets with different items of two sets
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ed75cd2e3c6dfbeb06e97f91bcae6081b16462ed/images/day9(symmetric%20difference).png)  
### 4. difference() and difference_update()
difference() gets items that are not similar from original sets and difference_update() update the sets with difference items from original sets.
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ed75cd2e3c6dfbeb06e97f91bcae6081b16462ed/images/day9(difference).png)
  
# Day10
### Other sets methods
Some of other sets methods that we can use are:
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/ee1483cb0912d16477f904b686c16efa6aa44304/images/day10.png)
    
# Day11
### Dictionaries in python
Dictionaries are ordered collection of data items. They store multiple items in a single variable.Dictionaries items are key-value pairs that are separated by commas and enclosed with curly brackets.Dictionaries doesnot allow duplicate items.
    
    dict={"name":"ram",
    "age":"21"}
    print=(dict)
    
![alt text](https://github.com/Peterpaudel/100Daysofcode/blob/05603fe735eb03a71ef43ab42451e6a734385372/images/day11.png)
# Day12
### Dictionaries methods in python
There are lots of methods in dictionaries some of them are listed below:

#### 1. update()
The update() methods update the values of the key provided else creates a new key:value pairs if the key used in update doesn't exists in that dictionaries.
<br>
<b>Example:</b>

    dict1={234:12,235:89,238:23}
    dict2={234:17,239:45}
    dict1.update(dict2)
    
Here,Since value of key 234 already exists i.e 12 gets overwrite as 17 dueto update methods
whereas new key value pair is updated on dict1 i.e 239:45.
sample program for update method is given below:<br>
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/e46d1007b83309e71906f7a6261010287e58e5a2/images/day12.1.png)
    
#### 2. Removing items from dictionaries:
    
#### pop() and del :
    
pop() methods is used to remove key value pairs from dictionary and del is used to remove entire dictionary.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/248b24013cd46f95ab08af716b515efed28013a3/images/day12.2.png)
    
For learning more about [dictionaries](https://docs.python.org/3/tutorial/datastructures.html)

# Day 13
Today I am creating KBC(Kaun banega crorepati) using my concepts of loop and list .
Here is the code ,Hope you get some insight
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/9ce08a5f1457450bc356db10fe018b6a00d40c13/images/day13.png)
# Day 14
### Exception handling :
Exception handling is the way of dealing with unwanted errors in programs.
one of the way of exception handling by using try and except
### try and expect:
#### Syntax: 
    
    try:
     #statements which could generate 
     #exception
    except:
     #Soloution of generated exception
     
#### Example :
    
    try:
      num = int(input("Enter an integer: "))
    except ValueError:
      print("Number entered is not an integer.")
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/2bc8234800f2617978c7a5b232cbcb75007cd49d/images/day14.png)
    
### Finally clause:
Finally is also type of exception handling  it is use when some statement or code had to be excecuted anyway .
finally is executed no matter what error occured or not (it also executed if it is running after return 0)
### Syntax: 

              try:
             #statements which could generate 
             #exception
          except:
             #solution of generated exception
          finally:
              #block of code which is going to 
              #execute in any situation
    
### Example:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b42bf4f6336259efaca9453664ad69e8547022a7/images/day14.1(finally%20exception%20handling).png)
    
### Output:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b42bf4f6336259efaca9453664ad69e8547022a7/images/day14.3(finally%20output).png)

    
    

    
    
   

    
    
    


 

# Update coming tomorrow

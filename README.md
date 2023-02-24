# 100Daysofcode
### Welcome to my journey of 100 days of coding I will be starting from python basic to advance
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/e7ee7319e636cdee1503cfe6611303c2a91d5b28/images/100daysofcode.png)
| Projects Completed|
| -------- |
|1.[**Rock,paper and scissors**](https://github.com/Utshav-paudel/python-project/blob/52492569a6fd370715038381271212741a8f8256/day4.6%20rock%20paper%20scissore.py)|
|2.[**Kaun bangega crorepati**](https://github.com/Utshav-paudel/python-project/blob/f245d82d6a740061001ef4e8759fc683a4879e18/KBC.py) |
|3.[**Coffee machine**](https://github.com/Utshav-paudel/100Daysofcode/blob/ca68172d64863eb80a029d209471cde284b7fb24/code/day25/main.py)|
|4.[**Betting on turtle race game**](https://github.com/Utshav-paudel/100Daysofcode/blob/ffa55b2723c0efa577db88d91162810966088a0e/code/day31/tutlerace.py)|
|5.[**Snake game**](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day35)|
### Core python 
|**Core python**|
|---------------|
|1.Language Fundamentals|
|2.Operators|
|3.Input and Output statements|
|4.Flow Control|
|5.Strings|
|6.List Data Structure|
|7.Tuple Data Structure|
|8.Set Data Structure|
|9.Dictonary Data Structure|
|10.Functions|
|11.Modules|
|12.Packages|


# Day 1
<p>Today I learned some basics in python like data types in python and about typecasting in python.
There are two types of typecasting in python </P>
1.Implicit typecasting:
conversion data types by program itself for e.g: 
  
```
  a=10
     b=2.0
     sum=a+b
     print(sum)
     #sum will be in float because of implicit typecasting
   
 ```
 
2. Explicit typecasting:
conversion of data types by programmer is called explicit typecasting .
  for e.g :
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
  
<p>Here is day2 codes I have learned about string slicing . String in python is similar to array .
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
    
### Then it convert time into string using
 
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
   
It is a sequence data types in python that is a collection of sequence of  elements.
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
     
It gives index of first occurence of the list item
    
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

# Day13
Today I am creating KBC(Kaun banega crorepati) using my concepts of loop and list .
Here is the code ,Hope you get some insight
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/9ce08a5f1457450bc356db10fe018b6a00d40c13/images/day13.png)
# Day14
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

In the above index is out of range so error occured and code inside except: is executed and after that code inside finally: is executed.Code inside finally: is executed whether error occurs or doesnot occurs.
# Day15    
#### Raising custom error in python 
In python, we can create custom error by using `raise` keyword .
We raise error to throw the exception from program .
Lets see a example:
** Objective: **To throw error if user enter number not between 1-4.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/896630d72319225dedf3c67fec86cd2da61bbcda/images/day15.png)
    
### if....else in one line
There is a shorthand syntax for if...else statement that can be used when condition is simple and codeblocks to be executed is short.
`Caution:`It is not used when codeblock is long and complex as this reduce code readability.
Here is a sample example :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/4fce9737af324129a0bb28d60b2aeca04d994257/images/day15.1(shorthand%20if%20else).png)
    
# Day16
### Object Oriented Programming
lets get start with some difference betweem POP and OOP
Procedure Oriented Programming(POP): Total activity is divided into multiple functions and we call those based on our requirements.
Object Oriented Programming(OOp) : Total activity is divided into realtime entities called objects.
* **Class** : Class is a blueprint/model which contains different entity inside it like properties(variable) and method(actions) which is inherited by objects.
* **Objects** : Objects is the physical existence of class.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/12ea7a5ff67055b3d7e5119c666257236970d312/images/day16%20class%20and%20object%20difference.png)
    
Here is a simplest program that reflects OOP in python :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/12ea7a5ff67055b3d7e5119c666257236970d312/images/day16%20(class%20and%20objects).png)

# Day17
### File handling 
Before performing any operation on file we have to know about the modes of file handling 
* Read : 'r' it allows reading file 
* Write : 'w' it allows to write in file 
* Append : 'a' it allows to append in file

Here is simplest program to clear your basic in filehandling
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/bd7fb9cd630c002e2432142a9ace11fefbfde348/images/day17.png)    

You can practice more on file handling [Click here for read in filehandling](https://github.com/Utshav-paudel/100Daysofcode/blob/d8e2e0436a7fd8c63329e93ccceb0e8546abf2c1/jupyternotebook/filehandling%20read%20file.ipynb)

You can practice more on file handling [Click here for write in filehandling](https://github.com/Utshav-paudel/100Daysofcode/blob/d8e2e0436a7fd8c63329e93ccceb0e8546abf2c1/jupyternotebook/filehandling%20write%20file.ipynb)
 
    
# Day18
### Enumerate funciton in python:
Enumerate function is a built in function in pythons that allows you to loop over a sequence such as list,tuple,string and get the `index` and value of element at the sametime. Some basic examples on how it works are shown below :
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b5a1f1590a9914ddbf2d392fd229f74db8e2411e/images/day18.png)
# Day19
### Importing in python:
Importing in python is the process of loading code from a python module to the current script.This allows you to use functions and variables defined in the module in your current script. You can simply import any module by writing import followed by the name of the module.
for e.g:
```python
import math
```
After importing math function as shown above you can use various function provided by math module like sqrt(),floor() and manymore

sample:

```python
    import math 
    square_root=sqrt(9)            
    floor_number=floor(4.676)
```
### from keyword
from keyword is used to import specific function from module .
```python
    from math import sqrt
```
### importing everything
we can everything available on module by using  from followed by module* But this isnot recommended because it make harder to understand where the specific function and variables are coming from.
```python
from  math import*
```
### The 'as' keyword
We can rename the module in python by the use of as keyword 
for e.g:
```python
import pandas as pd
import math as m
```
### The dir function
Python has built in function dir that allow you to view all the functions and variable available in modules.It help to understand and explore new module .
    
for e.g:
```python
import math
print(dir(math))
  ```

# Day20
### if ```__name__=="__main__"``` in python
This is a common idom used in python to determine whether the module imported should run directly or use as module . So  when we import any module it get executed 
directly in our script and to avoid this direct execution we used ```__name__=="__main__"```.
one sample is given below:
### Before using ```__name__=="__main__"```
We can see that welcome() function is running directly after importing side module in main script and output get printed twice one from direct execution of module and another from calling of function after importing module.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/51c29591d43b7ef38334668f064a292911f3c2b8/images/day20(before%20using%20of%20name==main%20idom).png)
### After using **__name__=="__main__"** welcome() function is not executed direclty.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/dcc57ae4b1f1bc69e4ccb430621ee6d75f31227f/images/day20(after%20using%20name==main%20idom).png)
So the main use of ```__name__=="__main__"``` is to import any module without running it functions directly.
   
   
# Day21
### Lambda Function 
This funcion is also known as anonymous function in python because it does have any name like function but behaves like function
syntax:
```lambda_expression= lamda (parameter list)=expression```
For e.g:
```python
f= lambda a:a*a
print(f(5))
```
Above lamda function is used to find square

# Day22
### Webscrapping 
Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user.

* first we will install request library by using requests library, we can fetch the content from the URL given
```python
pip install requests
```
* Also we will install beautiful soup that helps to parse(change format) data and fetch the details the way we want. You can use a beautiful soup library to fetch data using Html tag, class, id, css selector and many more ways.
```python
pip install beautifulsoup4
```
I am going to show you a sample of scrapping method and final results of it in excel file 
* Scrapped website [Link](https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets)
* Code that has done scrapping is given below :
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/dd706441cafaa4e1374d620215a33d6134d467f7/images/day22.png) 
    
* beautiful data after scrapping:
    
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0937bf6d6fde35fd2c7c0965845035a08dfd9a86/images/day22(scrapped%20data).png)

You can learn more on HTTP and requests [from here](https://github.com/Utshav-paudel/100Daysofcode/blob/46d4893b6d0336ee3b33359efd3e99db92595aa3/jupyternotebook/Requests_HTTP.ipynb)
    
# Day23
Today we are applying our learning and scrapping data from website of tata ipl auction 2022
* Here is the sample code that does all our scrapping:
  
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/35ba7e062a60e3cca244f7831414672860a23ef3/images/day23.png)
    
* Data obtained after scrapping:
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/35ba7e062a60e3cca244f7831414672860a23ef3/images/day23(scrapped%20data).png)
# Day24
### Map,reduce and filters function in python.
In python map,reduce and filters are built in function that allows you to apply a function to the sequence of element and returns a new sequence.These functions are called higher order function because they takes functions as arguments.
```Note:we can use lamda fucntion to make it more easier and efficient```
lets learn each of them .
* <strong>Map function</strong>
Map function simply performs the function on the given iterable sequence and return a whole new sequence of data.
 syntax:
 ```python
 map(function,iterable)
 ```
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(map).png)
 
 * <strong>Filter</strong>
 Filter simply filter the sequential data according to our defined predicates(i.e function) and give us selected data that passes condition after filtering.
 syntax:
 ```python
 filter(predicate_function,iterable)
 ```
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(filter).png)
 * <strong>Reduce</strong>
 ```python
 from functools import reduce
 reduce(function,iterable)
 ```
 Return is also similar higher oder function but it returns a single value output not  a list or sequence of data and ```it needs to be imported from functools.
    
   
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/692398c8ed0bfccf5fdccb0b4807542fbe595553/images/day24(reduce).png)
 # Day25 
 Today I created a project using python which is coffe machine.
 [Click here for its code](https://github.com/Utshav-paudel/100Daysofcode/blob/ca68172d64863eb80a029d209471cde284b7fb24/code/day25/main.py)
 
 # Day26
 ### Importing packages reading its documentation and using it
 Python has lots of library to use we can simply use it by installing it ,importing it and reading documentataion to use it.
 Here is the sample of me using ```PrettyTable``` library by installing it,importing it.
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0bfb546b7ef1bdab706db6577c289aa31a91d0a2/images/day26.png)
 
 # Day27
 #### OOP is the main usecase of python and many other programming languages that solves realworld problems.
 In Day16 We have discussed basic of object and class . Today we are going to discuss about different concepts of OOP in python like:
 * #### The ```__init__()``` function
 This function is always initiated when the class is being iniated . It passes values to object properties, or other operations that are necessary to do when the object is being created.
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3e4c59900ab511763c3cf1a6d52b7930084ffc2b/images/day27(the__inti__function).png)
 
* #### The ```__str__()``` function
The __str__() function controls what should be returned when the class object is represented as a string.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/a22df59805b9fae296b85010c70f6ced44729672/images/day27(__str__()fucntion).png)
    
#### Objects method
Objects method is the function in objects. Let create a sample object method 
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f1773e78980e3265bfb41864e25425d422bfd38f/images/day27%20object%20method.png)

# Day28
### Turtle graphics and using it to make arts :
Before learning about turtle graphics let us see about importing ways once.
* from import_module import class_or_function 
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f0dca120c71e4bdab1aa5a80bc1f1426d54f4cae/images/day28(import%20).png)
* from import_module import*
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f0dca120c71e4bdab1aa5a80bc1f1426d54f4cae/images/day28%20import%20everything.png)
    
 Always remember to break down your poblem,write pseudo code and start coding .
 Here is a sample solution of problem that I created ,You can understand problem and solution by reading code and comments.
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3288dd683cf5cf459ada2cdc25257dded1fa2d9a/images/day28%20problem.png)
    
 Output:
    
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/3288dd683cf5cf459ada2cdc25257dded1fa2d9a/images/day28%20solving%20problem%20output.png)
 
 # Day29
 ### Problem: Create a random walk with random color
 * solution:
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0a77accbd3ae73c6875ff21a04b9300f22838f95/images/day29randomwalkcode.png)
 * output:
    
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0a77accbd3ae73c6875ff21a04b9300f22838f95/images/day29random%20walk.png)
 
 ### Creating spirograph 
 * code:
    
 ![spirograph code](https://github.com/Utshav-paudel/100Daysofcode/blob/9eaa626c9feb758282143e25e363f47a9cfd301a/images/day29%20spirograph.png)
   
* Output:
    
 ![spirograph output](https://github.com/Utshav-paudel/100Daysofcode/blob/9eaa626c9feb758282143e25e363f47a9cfd301a/images/day29%20creating%20spirograph.png)
 
 # Day30
 Today I learned to create hirst painting which is sold in millon dollars in muesum using python.
 This learning is helping me to build strong problem solving and programming logic .
 * **Hirst painting** : We have to create similar painting
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30%20objective.png)
 
 * **Code**: My code is as follow
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30%20code.png)
 
 * **Output** : Here is final result
 
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/07b647d65d941915f02ffc28316f4ed7cfe67e18/images/day30.png)
 
 # Day31
 ### Working with turtle graphics 
 #### Creating drawing app
 Using turlte I created a screen where user can draw and erase by themself
#### CODE
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f27f65a5ba91f9fc9cf937e0aa573df4a47358b0/images/day31.png)
#### Output
 ![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/f27f65a5ba91f9fc9cf937e0aa573df4a47358b0/images/day31%20drawing%20output.png)
# Day32 
## Turtle Betting race game
I have created a very fun project where six different color turtle are racing , you can bet on any color of turtle and at last winner turtle will be declared,If winner is similar to bet you will won .
This projects has been very fun it uses many concepts of python like loop,list,modules.
Here is a code for this project hope you get some insight
# Code
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20code.png)
# Input prompt
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20bet.png)
# Output
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/b47727bec31d5cf6320b86733522330877a9265a/images/day31%20output.png)

![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/cbda82c04134fe491e03e3feb42abfcd912c43d9/images/day32%20final%20output.png)
# Day33
Today I started to create snake game and it challenge my logic to core mainly to create the movement of segment it was challenging.
### Task completed so far:
* screen
* snake body
* segment movement , snake movement
Here is a code which will be completed tomorrow for full game
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/0f882e0afff37ca7bd0939b10db86f1ef29f1029/images/day33%20snake%20code.png)
    
# Day34
Today I continued snake game and made snake to move according to botton,created food,made snake to eat food .
It is still incomplete
### Task completed so far:
* movement of snake
* food
* consuming food by snake
You can check the code of till data [here](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day34)

# Day35
Today I completed the snake game and in total it was awesome and very fun projects . 
Here is sample of how game looks like
![snake game ](https://github.com/Utshav-paudel/100Daysofcode/blob/76b67320225331b9a7b0cabf6d23d6536129fad9/images/day35.png)

You can check this game by 
* first run this on terminal
```pip install turtle```
* And download [this](https://github.com/Utshav-paudel/100Daysofcode/tree/Utshav-paudel/code/day35) and run 

# Day36
Today I continued my learning on webscraping and scraped a website .
* **note**: find_all create list
Here is a sample code that find joblist from timejobs website.
![alt text](https://github.com/Utshav-paudel/100Daysofcode/blob/833ceaf26e7f591ab934d5c0d6952ed4c83cb277/images/day36%20.png)


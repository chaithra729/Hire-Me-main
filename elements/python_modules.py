test your c skills - yashwanth kanetkar
let us c 
test your c++ skills
let us c++

python tutorial:
w3 schools
geeksforgeeks
javatpoint
programiz.com
prepbytes
prepinsta

c ? - dennis ritche
- mother language
- compiler language
- procedural oriented
- mid level programming language

// - single line comment
/* */ - multiline comment

machine language- 0s 1s 
assembly level - mov a,b --add a,b--sub a,b
c - mid level ---c=a+b
c++ - procedural+object oriented
java - object oriented
python - high level programming language

- guido van rossum
- interpreted language

# - single line comment
''' multi line comment''' 


.c 
.cpp
.py 





a = 5
b = 6
print(a+b)

#variables 
udupi_123
_123udupi
UDUPI123
123udupi
**123udupi 

CASES:
1. Camel Case :

rockSalt 
brownSugar 
rawRice
2. Pascal case
    RockSalt 
    RawRice
    PinkSalt
3. snakecase 
    rock_salt_may 
    RAW_RICE_AUG
4. Kebab Case 
    rock-salt-may
    raw-rice-aug


   
    
    













https://www.swiggy.com/restaurants/asha-sweet-center-since-1951-gandhi-bazaar-basavanagudi-bangalore-160120



Cases : 
Dal 
salt 
Sugar 

toordal 
moongdal
rocksalt
pinksalt
brownsugar
1. Camel Case 
toorDal 
moongDal
rockSalt

2. Pascal Case
MoongDal
PinkSalt
BrownSugar
3. Snake Case 
moong_dal_jan 
PINK_SALT_OCT
4. Kebab Case  - name of the URLs
lower case 
 moong - dal - jan














#variables

atme_eee  - v
eee-atme -x
ATMEEEE -v
_atme_eee - v
atme eee - x
123atme - x
atme123eee - v
$atmeeee - x

#cases
1. Camel Case
atmeEee
whiteRice
brownRice
basmatiRice

2. Pascal Case
WhiteRice
BrownRice
BasmathiRice

3. Snake Case - lower case or Upper case
brown_rice_vijayanagar
WHITE_RICE_GOKULAM

4. Kebab Case - lower case
white-rice-vijayanagar
name of the URL - application


AtmeEee
atme_eee_mysore
ATME_EEE_MYSORE
atme-eee-mysore









#multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpacking
fruits = ["apple", "banana", "cherry"]#list 
x, y, z = fruits
print(x)
print(y)
print(z)

#cancatenation
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # cancatenation

#
x = 5  #int 
y = "John" #string
print(x,y) #5 john

#
x = 5
y = "John"
print(str(x) + y)

m1 = "Srinivasa Kalyana"
r1=4.8
m2= "KGF"
r2= 4.7
m3 ="Pataan"
r3 = 4.6 
o/p : srinivasa Kalyana-4.8 

1. Local 
2. Global
3. Static - static - local & global 
4. automatic - auto - local 
5. external - extern - global 






#Global Variables
x = "awesome"
def myfunc():       #function definition
  print("Python is " + x)
myfunc() #fun call

#
x = "awesome" #global
def myfunc():
  x = "fantastic" #local
  print("Python is " + x)
myfunc()
print("Python is " + x)

#If you use the global keyword, 
#the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"
myfunc() #fun call
print("Python is " + x)

#
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#
#creating local variables
def f():
    s="I love Python"
    print(s)
f()  
#
# Declaring a function  
def add():  
    # Defining local variables. 
    #They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
add()  # Calling a function 

 
#local cannot be accessed outside the function
def f():
    s="I love Python"
    print(f"Inside function:{s}")
    #format string , place holder
f()
print(s)

#define global variable 
def f():
    print(f"Inside function:{s}")
    #f - format string
s="I love Python"
f()
print(f"Outside function:{s}")

#same name for local and global
def f():
    s="Me too"
    print(f"Inside function:{s}")
s="I love Python"
f()
print(f"Outside function:{s}")

#cant modify global inside function
def f():
    s=s+"programming"
    print(s)
s="I love Python"
f()

#use global keyword for change and assign 
#global variable inside function
def f():
    global s
    s=s+" programming"
    print(s)
s="I love Python"
f()


#modify global
def f():
    global s
    s=s+" programming"
    print(s)
    s="Python is great"
    print(s)
s="I love Python"
f()
print(s)


#using python local and global variables
a = 1
def f():
    print('Inside f() : ', a)#1
def g():
    a = 2
    print('Inside g() : ', a) 
def h():
    global a
    a = 3
    print('Inside h() : ', a)
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a) 
h()
print('global : ', a) 
# Static variable 
# 






Data TYPES  - Number Data Types
a = 5  # int
print("Type of a: ", type(a)) #<class int>
b = 5.0  # float
print("\nType of b: ", type(b)) 
c = 2 + 4j  #complex
print("\nType of c: ", type(c))

#strings
str = "string using double quotes"  
print(str)  
s = '''A multiline 
string'''  
print(s)  

#
str1 = 'hello smvit' #string str1    
str2 = ' how are you' #string str2    
print (str1[0:2]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    
print (str1*2) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2    
#
String1 = "pe"
print(String1) #p
print(String1[0]) #first character p
print(String1[-1]) #last character p

#
Lists in Python are like arrays in C, 
but lists can contain data of different types. 
The things put away in the rundown are isolated 
with a comma (,) and encased inside square 
sections [].

To gain access to the list's data, 
we can use slice [:] operators. 
Like how they worked with strings, 
the list is handled by the concatenation 
operator (+) and the repetition operator (*).

#
List = []  
print(List)  #[]
List = ['smvitcollege'] 
print(List) 
List = ["smvit", "aiml", "college",1,1.3,'c'] 
print(List[0]) 
print(List[2]) 
List = [['smvit', 'aiml'], ['college']] 
#nested list 
print(List) 


#
List = ["love", "python", "language"] 
print(List[0]) 
print(List[2]) 
print(List[-1]) 
print(List[-3]) 

#
list1  = [1, "hi", "Python", 2]    
print(type(list1))  #<class list >
print (list1)  
print (list1[3:])  
print (list1[0:2])   
print (list1 + list1)   
print (list1 * 3)  #repetition operator

#
Just like a list, a tuple is also an ordered 
collection of Python objects. 
The only difference between a tuple and a list 
is that tuples are immutable i.e. 
tuples cannot be modified after it is created. 
It is represented by a tuple class. 

#
Tuple1 = () 
print(Tuple1) #()
Tuple1 = ('smvit', 'aiml') 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print(tuple(list1))  #(1,2,4,5,6)
Tuple1 = tuple('smvit') 
print(Tuple1) #
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'programming') 
Tuple3 = (Tuple1, Tuple2) 
print(Tuple3) 
#((0,1,2,3),('python','programming'))

#
tuple1 = tuple([1, 2, 3, 4, 5]) 
print(tuple1[0]) 
print(tuple1[-1]) 
print(tuple1[-3]) 

#
tup  = ("hi", "Python", 2)    
print (type(tup))    
print (tup)  
print (tup[1:])    
print (tup[0:1])    
print (tup + tup)    
print (tup * 3)     
tup[2] = "hi"  


#
fruits = ["apple", "banana", "orange"] 
print(fruits) 
fruits.append("grape") 
print(fruits) 
fruits.remove("orange") 
print(fruits)

#bool
print(type(True)) 
print(type(False)) 
print(type(true)) 

#SET 
In Python, a Set is an unordered collection 
of data types that is iterable, mutable, 
and has no duplicate elements. 
The order of elements in a set is undefined 
though it may consist of various elements.
#sets using different types of values, 
#such as strings, lists, and mixed values
set1 = set() 
print(set1) #()
set1 = set("pescollege") 
print(set1) 
set1 = set(["Geeks", "For", "Geeks"]) 
print(set1) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print(set1) 


#
set1 = set(["pes", "civil", "college"]) 
print(set1) 
for i in set1: 
	print(i, end=" ") 
    
#
set1=set([])
print("atme" in set1)
#
set1 = set()  
set2 = {'James', 2, 3,'Python'}  
print(set2)  
set2.add(10)  
print(set2)  
set2.remove(2)  
print(set2) 

#Dictionary
A dictionary is a key-value pair set arranged 
in any order.
It stores a specific value for each key, 
like an associative array or a hash table. 
Value is any Python object, while the key can 
hold any primitive data type.

The comma (,) and the curly braces are used 
to separate the objects in the dictionary. 

#
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
print (d)  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
print (d.keys())    
print (d.values()) 



#
Dict = {1: 'atme', 'name': 'For', 3: 'college'} 
print(Dict['name']) 
print(Dict.get('name')) 

#
student_id = {112, 114, 116, 118, 115}
print(student_id)
print(type(student_id))



#
capital_city = {'Nepal': 'Kathmandu', 
'Italy': 'Rome', 'England': 'London'}
print(capital_city)

# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 
'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])  
print(capital_city['Kathmandu'])

1. Arithmtic 

+, -, * , /, //, **
#
9/4 = float division = 2.22
8//4 = floor/integer division= 2

#ceil() - rounds up the value
ceil(3.6) = 4.0
ceil(3.2) = 4.0 
ceil(4.3) = 5.0 
#floor() - rounds down the value 
floor(4.8) = 4.0
floor(7.2) = 7.0 
floor(5.5)=5.0
#round() = 
round(4.6) = 5.0 up 
round(4.4)= 4.0 down 
round(4.499999) = 4.0 
round(4.5) = 5.0 














#
a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 

#
a = 5
b = 6
print((a > 2) and (b >= 6)) 

#
print(True and True)     # True
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

#relational 
==, != , >,<,>=,<=

#assignment opeartor
+= , -=, *=, /=, //=, %=, and=, or=, &=,|=
^=, ~=, <<=, >>= 

a= 6
b=5 
c=a+b
a+=b ====11 
DRY -  
calloc
malloc
realloc
free()

a = 20 , b=13
a & b = bitwise AND 


















#special Operators
#1. Python Identity Operators - 'is', 'is not'
a = 10
b = 10
c = a 
print(a is not b) 
print(a is c)

#
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)  
print(x3 is y3) 

#
a = ["Rose", "Lotus"]  
b = ["Rose", "Lotus"]  
c = a 
print(a is c)   #True
print(a is not c)   # false
print(a is b)  #false
print(a is not b)  #true 
print(a == b)  
print(a != b)   

#2.Membership Operators in Python:'in' 'not in'
x = ["Rose", "Lotus"]  
print("Rose" in x)  
print("Riya" not in x) 
#
x = 24
y = 20
list = [10, 20, 30, 40, 50] 
if (x not in list): 
	print("x is NOT present in given list") 
else: 
	print("x is present in given list") 

if (y in list): 
	print("y is present in given list") 
else: 
	print("y is NOT present in given list") 

#
x = 'Hello world'
y = {1:'a', 2:'b'}
print('H' in x) 
print('hello' not in x)
print(1 in y) 
print('a' in y) #always key value

#Ternary Operator in Python 
a, b = 10, 20
min = a if a < b else b 
#[value1] if [expression] else [value2]
print(min) 

#
a, b = 2, 5
max = a if a > b else b 
print('Maximum :', max)

#Print statements in ternary operator
a, b = 2, 5
print('Python') if a > b else print('Examples')

# Nested ternary operator
a, b, c = 15, 93, 22
max = a if a > b and a>c else b if b>c else c
print(max)

# 10,45,62,34  max
#
a, b = 10, 20
num = a if a > b else b if a < b else a
print(num)

#
age = 25
print("Can vote" if age >= 18 else 
"Can not vote")

#
a, b = 10, 20
print("a is greater than b" if a > b else 
"a is less than b")

#
num = int(input("Enter a number: "))
num = 10 if num > 10 else num
print(num)

#Here is an example of 3 nested ternary operators.
a, b = 12, 30
divA = "No" if (a % 2 != 0) else ("No" 
if (a % 3 != 0) else ("No" if (a % 5 != 0) 
else "Yes"))
divB = "No" if (b % 2 != 0) else ("No" 
if (b % 3 != 0) else ("No" if (b % 5 != 0) 
else "Yes"))

print(divA)
print(divB)

#Ternary Operator Multiple Conditions
a, b = 12, 30
divA = "Yes" if (a % 2 == 0 and a % 3 == 0 
and a % 5 == 0) else "No"
divB = "Yes" if (b % 2 == 0 and b % 3 == 0 
and b % 5 == 0) else "No"

print(divA)
print(divB)

#Python Ternary Operator Without Else
a, b = 10, 20

result = (a < b) and "a is less than b"
print(result)

The above code has the format of True/False 
and string
If the first statement is false then the 
and operator will return False & the second 
statement will not be executed.

If the first statement is true then 
the and operator will return second statement.

#assigning grades (A, B, C) based on marks 
#obtained by a student.

if the percentage is above 90, assign grade A
if the percentage is above 75, assign grade B
if the percentage is above 65, assign grade C

#
number = -1
# check if number is greater than 0
if number > 0:
    print('Number is positive.')
print('The if statement is easy')


#IND - indeterminate 
#-nan 


#check number 0, +ve, -ve
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

#
number = -2
if (number >= 0):
    if number == 0:
      print('Number is 0')
    
    else:
        print('Number is positive')

else:
    print('Number is negative')

# even or odd number
num = int(input("enter the number:"))         
if num%2 == 0:      
    print("The Given number is an even number") 

#Program to print the largest of the three numbers.
a = int (input("Enter a: "));    
b = int (input("Enter b: "));    
c = int (input("Enter c: "));    
if a>b and a>c:    
    print ("a is largest");    
if b>a and b>c:    
    print ("b is largest");    
if c>a and c>b:    
    print ("c is largest");       
    
#Program to check whether a person is eligible to vote or not.
age = int (input("Enter your age: "))    
if age>=18:    
    print("You are eligible to vote !!");    
else:    
    print("Sorry! you have to wait !!");  

#
# python program to illustrate If statement 

i = 100
if (i > 15): 
	print("10 is less than 15") 
print("I am Not in if") 

#
# python program to illustrate If else statement 
#!/usr/bin/python 

i = 10
if (i < 15): 
	print("i is smaller than 15") 
	print("i'm in if Block") 
else: 
	print("i is greater than 15") 
	print("i'm in else Block") 
print("i'm not in if and not in else Block") 

#
# Python program to illustrate 
# Iterating over a list 
l = ["atme", "for", "college"] 
for i in l: 
	print(i) 

#
# Iterating over dictionary 
print("Dictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d: 
	print("% s % d" % (i, d[i])) 
    
#
languages = ['Swift', 'Python', 'Go', 
'JavaScript']
for language in languages:
    print(language)
    
#
for x in 'Python':
    print(x)

#
# use of range() to define a range of values
values = range(2)
# iterate from i = 0 to i = 3
for i in values:
    print(i)


##It is not mandatory to use items of a 
#sequence within a for loop. 
languages = ['Swift', 'Python']

for i in languages:
    print('Hello')
    print('Hi')
    
#The _ symbol is used to denote that the 
#elements of a sequence will 
#not be used within the loop body.
languages = ['Swift', 'Python', 'Go']
for _ in languages:
    print('Hello')
    print('Hi')
    
# for loop with else
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")
#
fruits = ["apple", "banana", "cherry",'orange']
for x in fruits:
  print(x)
  if x == "cherry":
    break

#
fruits = ["apple", "banana", "cherry", orange,'kiwi']
for x in fruits:
  if x == "orange":
    continue
  print(x)
  
#
for x in range(6):
  print(x)
  
#while loop

# Python program to illustrate 
# while loop 
count = 0
while (count < 3): 
	count = count + 1 
	print("Hello pes")
    
#
age = 28
# the test condition is always True 
while age > 19: 
	print('Infinite Loop')




# Prints all letters except 'e' and 'm' 
i = 0
a = 'pescollegemandya'
while i < len(a):  #16
	if a[i] == 'e' or a[i] == 'm': 
		i += 1
		continue	
	print('Current Letter :', a[i]) 
	i += 1
#
# break the loop as soon it sees 'e' 
# or 's'

"python programming language"









 
i = 0
a = 'pescollege'
while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		break	
	print('Current Letter :', a[i]) 
	i += 1

#
# An empty loop 
a = 'pescollege'
i = 0
while i < len(a): 
	i += 1
	pass	
print('Value of i :', i) 

#
# checks if list still 
# contains any element 
a = [1, 2, 3, 4] 
while a: 
	print(a.pop())

#
countdown = 10
while countdown > 0: 
	print(countdown) 
	countdown -= 1
print("Blast off!") 

#
initial_height = 10
bounce_factor = 0.5
height = initial_height 
while height > 0.1: 
	print(height, "meters.") 
	height *= bounce_factor 
print("The ball has stopped bouncing.")


#
i = 1
while i < 6:
  print(i)
  i += 1
  
#
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) 
#
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
#
i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

#
# program to calculate the sum of numbers
# until the user enters zero

total = 0
number = int(input('Enter a number: '))
while number != 0:
    total += number    # total = total + number
    
    number = int(input('Enter a number: '))
print('total =', total)

#
counter = 0
while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
    
#
counter = 0

while counter < 3:
    if counter == 1:
        break
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')
    
'''Note: The else block will not execute 
if the while loop is terminated by a 
break statement.'''

#
# break statement example  
my_list = [1, 2, 3, 4]  
count = 1  
for item in my_list:  
    if item == 4:  
        print("Item matched")  
        count += 1  
        break  
print("Found at location", count)  

#
# break statement example  
my_str = "python"  
for char in my_str:  
    if char == 'o':  
        break  
    print(char) 

#
# break statement example  
i = 0;    
while 1:    
    print(i," ",end=""),    
    i=i+1;    
    if i == 10:    
        break;    
print("came out of while loop");

#
# break statement example  
n = 2  
while True:  
    i = 1  
    while i <= 10:  
        print("%d X %d = %d\n" % (n, i, n * i))  
        i += 1  
    choice = int(input("Do you want to 
    continue printing the table? Press 0 
    for no: "))  
    if choice == 0:  
        print("Exiting the program...")  
        break  
    n += 1  
print("Program finished successfully.")  

#
# program to find first 5 multiples of 6

#program to print odd numbers from 1 to 10 
#using continue


#nothing happens when the pass is executed. 
It results in no operation (NOP)

n = 10
# use pass inside if statement
if n > =10:
    pass
print('Hello')

#
n = 10

if n > 10:
    # write code later

print('Hello')

#
a = 10
b = 20

if(a<b):
    pass
else:
    print("b<a")

#Let’s take another example in which the 
#pass statement gets executed when the 
#condition is true.

# Using pass as a placeholder inside an if statement
x = 5
if x > 10:
	pass
else:
	print("x is less than or equal to 10")

def my_function():
	pass

class MyClass:
	def __init__(self):
		pass

#
# python code to demonstrate working of 
#enumerate()

for key, value in enumerate(['The', 'Big', 
'Bang', 'Theory']):
	print(key, value)

#
# python code to demonstrate working of 
#enumerate()

for key, value in enumerate
(['atme', 'for', 'college',
'is', 'the', 'Best','Coding', 'Platform']):
	print(value, end=' ')


#looping Techs
# Two different data type(list,tuple)
#combine
# python code to demonstrate working of zip()

names = ['Deep', 'Sachin', 'Simran']	 # list
ages = (24, 27, 25)		 # tuple

for i, j in zip(names, ages):
	print('Name: ', name)
	print('Age: ', age)
	print()

#
# python code to demonstrate working of zip()

questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

for i, j in zip(questions, answers):
	print('What is your {0}? I am {1}.
    '.format(i, j))
    
#Using iteritem(): iteritems() is used to 
#loop through the dictionary printing 
#the dictionary key-value pair sequentially 
#which is used before Python 3 version.




in c using "typedef" 
in python "alias" 

typedef reliance_iphone_board_fix R_I_Bug




#FUNCTIONS
#Creating Function
def my_function():
  print("Hello from a function")
  
#calling
def my_function():
  print("Hello from a function")
my_function()  # CALLING

#
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#
def my_function(fname, lname, SNAME):
  print(fname + " " + lname)
my_function("Emil", "Refsnes", "RIYA")

#Arbitrary Arguments are often shortened to 
#*args in Python documentations.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias"
, child3 = "Linus")

'''If you do not know how many keyword arguments 
that will be passed into your function, 
add two asterisk:  before 
the parameter name in the function definition.'''

def my_function(kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Arbitrary Kword Arguments are often shortened 
#to kwargs in Python documentations.
In Python, functions can accept arguments in various forms. Here are four types of arguments that Python functions commonly use:

1. Positional Arguments: 
    def greet(name, message):
        print(f"Hello, {name}! {message}")
    greet("Alice", "How are you?")
    

2. Keyword Arguments: 
    def greet(name, message):
        print(f"Hello, {name}! {message}")

    greet(message="How are you?", name="Bob")
    

3. Default Arguments: 

    def greet(name, message="Good morning!"):
        print(f"Hello, {name}! {message}")

    greet("Charlie")  # Will print: Hello, Charlie! Good morning!
    

4. Variable Length Arguments: 
    - Arbitrary Positional Arguments (*args):
    This allows a function to accept any 
    number of positional arguments. 
    The parameter name "args" is commonly 
    used, but any name preceded by an 
    asterisk (*) will work.
    
    - Arbitrary Keyword Arguments (kwargs): 
    This allows a function to accept 
    any number of keyword arguments. 
    The parameter name "kwargs" is 
    commonly used, but any name preceded 
    by double asterisks () will work. 
    These arguments are captured as a 
    dictionary where the keys are the 
    argument names and the values are their corresponding values.

    
    def greet(*names):
        for name in names:
            print(f"Hello, {name}!")

    greet("Alice", "Bob", "Charlie")

    def print_info(kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Alice", age=30, 
    city="New York")
    

'''These argument types offer flexibility 
in function parameter passing in Python,
 making it easier to work with different 
 types of data and scenarios.'''

##
A lambda function is a small anonymous 
function.

A lambda function can take any number 
of arguments, 
but can only have one expression.

syntax:
lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
##
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

##
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


#RegEx Module
Python has a built-in package called re, which 
can be used to work with Regular Expressions.
Import the re module:

'''Search the string to see if it starts with 
"The" and ends with "Spain":'''

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


findall-Returns a list containing all matches
search-Returns a Match object if there is a match 
anywhere in the string
split-Returns a list where the string has been split 
at each match
sub-Replaces one or many matches with 
a string

#Print a list of all matches:
"The rain in Spain"

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#
Return an empty list if no match was found:

import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#
Search for the first white-space character in 
the string:

import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is 
located in position:", x.start())

#Make a search that returns no match:
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

###Split at each white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

##
Split the string only at the first occurrence:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

##
Replace every white-space character with 
the number 9:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

###
Replace the first 2 occurrences:

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

##Do a search that will return a Match Object:

import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

##
Print the position (start- and end-position) 
of the first match occurrence.

The regular expression looks for any words 
that starts with an upper case "S":

import re
txt = "The rain in Spain" #12, 17, 
x = re.search(r"\bS\w+", txt)
print(x.span())

##Print the string passed into the function:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

'''Print the part of the string where there 
was a match.
The regular expression looks for any 
words that starts with an upper case "S":'''

import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


#Strings 
a = "hello"
b='world'
print(a,b)

#reassigning string
str = "HELLO"    
str[0] = "j"    
print(str)

#
str = "helloworld"  
del str[1]  

#
str1 = "helloworld"  
del str1  
print(str1)


#
str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) 
# prints The string str : Hello  


#escape sequences
str = "They said, "Hello what's going on?""  
print(str)  
# using triple quotes  
print('''''They said, "What's there?"''')  
  
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")

#
print("C:\\Users\\PES COLLEGE\\Python32\\Lib")  
print("This is the \n multiline quotes")  
print("This is \x48\x45\x58 representation")  


# format() in strings {}-place holders 
# Using Curly braces  
print("{} and {} both are the best friend".
format("Devansh","Abhishek"))  
  
#Positional Argument  
print("{1} and {0} best players ".
format("Virat","Rohit"))  
  
#Keyword Argument  
print("{a},{b},{c}".format(a = "James", 
b = "Peter", c = "Ricky")) 

# % opeartor
Integer = 10;    
Float = 1.290    
String = "PES"    
print("Hi I am Integer ... My value is %d\n
Hi I am float ... My value is %f\n
Hi I am string ... My value is %s"
%(Integer,Float,String)) 

# STRING in-built FUNCTIONS
#1. len(): Returns the length of the string.
 
   s = "Hello, World!"
   print(len(s))  # Output: 13
   
#2. capitalize(): Returns a copy of the 
#string with the first character capitalized.

   s = "hello, world!"
   print(s.capitalize())  # Output: Hello, world!
   
#3. upper(): Returns a copy of the string 
#with all characters converted to uppercase.
   
   s = "hello, world!"
   print(s.upper())  # Output: HELLO, WORLD!
   

#4. lower(): Returns a copy of the string 
#with all characters converted to lowercase.
   
   s = "Hello, World!"
   print(s.lower())  # Output: hello, world!
   

#5. strip(): Returns a copy of the string 
#with leading and trailing whitespace removed.
   s = "  Hello, World!  "
   print(s.strip())  # Output: Hello, World!
'''6. replace(): Returns a copy of the string 
with all occurrences of a substring replaced 
with another substring.'''
 
   s = "Hello, World!"
   print(s.replace("Hello", "Hi"))  # Output: Hi, World!
   
'''7. split(): Splits the string into a list 
of substrings based on a delimiter.'''
   s = "apple,banana,orange"
   print(s.split(","))  
   # Output: ['apple', 'banana', 'orange']
   

'''8. join(): Joins the elements of an 
iterable into a string, using the string as 
a separator.'''
   fruits = ['apple', 'banana', 'orange']
   print(",".join(fruits))  
   # Output: apple,banana,orange
   
'''9. find(): Returns the lowest index of the 
substring if found, otherwise returns -1.'''
   s = "Hello, World!"
   print(s.find("World"))  # Output: 7
   
'''10. count(): Returns the number of occurrences 
of a substring in the string.'''
 s = "Hello, World! Hello!"
 print(s.count("Hello"))  # Output: 2
    


#OOPS 
object oriented programming
- class & objects
python supports oops
<class int>
<class float>
<class complex>
<class str>


Truth Tables :
AND(x)
0  0    0
0  1    0
1  0    0
1  1    1

OR(+)
0 0     0
0 1     1
1 0     1
1 1     1

not 
0       1
1       0

XOR
0 0   0
0 1   1
1 0   1
1 1   0

a =10
b =20
c = a+b
3 mem locations

a=10
b=20
a+=b #a=a+b




#math functions

1. min() & max()
2. pow()
3. abs() - absolute value

import math  - module/ library in python 
4. ceil() - rounds up the value 
    ceil(4.6) = 5.0
    ceil(3.2) = 4.0 
5. floor() - rounds down the value 
floor(5.6) = 5.0
floor(3.2) = 3.0 
6. round() - 
    round(4.7) = 5.0
    round(3.2) = 3.0
    round(4.49999) = 4.0
    round(4.5) = 5.0 




#data structures 
#LIST, TUPLE, SET, DICTIONARY 
# CREATE , READ, INSERT, UPDATE, DELETE,SELECT
# CRUD IS 

#List Data Structures
#CREATION
1. Creating an empty list:

my_list = []  #[]

2. Creating a list with elements:

my_list = [1, 2, 3, 4, 5]

3. Creating a list with different data types:

mixed_list = [1, "apple", True, 3.14]

4. Creating a list using list comprehension:

squares = [x2 for x in range(10)]

5. Creating a nested list:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

6. Creating a list with repeated elements:
repeated_list = [0] * 5

#LIST COMPREHENSION
# Example 1: Generating a list of squares 
#of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  

# Example 2: Generating a list of even numbers 
#from 0 to 20
even = [x for x in range(21) if x % 2 == 0]
print(even)  

# Example 3: Generating a list of tuples 
#containing both the number and its square
number= [(x, x**2) for x in range(1, 6)]
print(number)   

# Example 4: Generating a list of strings 
#with each string capitalized
words = ["hello", "world", "python", "list", "comprehension"]
ca_words = [word.capitalize() for word in words]
print(ca_words)  

##Accessing elements in a list 
1. Accessing a single element:
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

2. Negative indexing:
print(my_list[-1])  # Output: 5 (last element)
print(my_list[-2])  # Output: 4 (second to last element)

3. Accessing elements through slicing:
(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])   # Output: [1, 2, 3] (elements from the beginning to index 2)
print(my_list[2:])   # Output: [3, 4, 5] (elements from index 2 to the end)


4. Accessing nested lists:
'''If your list contains nested lists, 
you can access elements of the nested 
lists using multiple indices.'''

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[2][1])  # Output: 4 (first element of the second nested list)


5. Accessing elements with steps:
You can specify a step value to skip elements 
while accessing them.

print(my_list[::2])  
# Output: [1, 3, 5] (elements with step 2)


#TRAVERSING
1. Using a for loop:

my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)


2. Using a for loop with range and len():
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i])

3. Using a while loop:

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1


4. Traversing through a nested list:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for sublist in nested_list:
    for element in sublist:
        print(element)

# FUNCTIONS

1. len(): Returns the number of elements in the list.
    
    my_list = [1, 2, 3, 4, 5]
    length = len(my_list)
    print(length)  # Output: 5
    

2. count(): Returns the number of occurrences of a specified element in the list.
    
    my_list = [1, 2, 2, 3, 2, 4]
    count = my_list.count(2)
    print(count)  # Output: 3
    

3. index(): Returns the index of the first occurrence of a specified element in the list.
    
    my_list = [1, 2, 3, 4, 5]
    index = my_list.index(3)
    print(index)  # Output: 2 (index of element 3)
    

4. append(): Adds an element to the end of the list.
    python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    

5. insert(): Inserts an element at a specified position in the list.
    python
    my_list = [1, 2, 3]
    my_list.insert(1, 1.5)
    print(my_list)  # Output: [1, 1.5, 2, 3]
    

6. extend(): Adds elements from another list 
(or any iterable) to the end of the list.
    
    my_list = [1, 2, 3]
    another_list = [4, 5, 6]
    my_list.extend(another_list)
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    

7. remove(): Removes the first occurrence of a specified element from the list.
    python
    my_list = [1, 2, 3, 2, 4]
    my_list.remove(2)
    print(my_list)  # Output: [1, 3, 2, 4]
    

8. pop(): Removes and returns the element at a specified index (by default, the last element).
    
    my_list = [1, 2, 3, 4, 5]
    popped_element = my_list.pop(2)
    print(popped_element)  # Output: 3
    print(my_list)  # Output: [1, 2, 4, 5]
    

9. reverse(): Reverses the order of elements in the list. 
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)  # Output: [5, 4, 3, 2, 1]
    
10. sort(): Sorts the elements of the list in ascending order (by default) or using a custom key function.
    
    my_list = [3, 1, 4, 1, 5, 9, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]
    
#nested lists to represent a matrix 

1. Creating a matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


2. Accessing elements:

# Accessing a single element
element = matrix[0][0]  # accessing the element in the first row and first column
print(element)  # Output: 1

# Accessing a row
row = matrix[1]
print(row)  # Output: [4, 5, 6]

# Accessing a column
column = [row[2] for row in matrix]  # extracting the third column
print(column)  # Output: [3, 6, 9]


3. Traversing through the matrix:

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # to move to the next line after printing each row

Output:

1 2 3 
4 5 6 
7 8 9 


4. Modifying elements:

matrix[1][1] = 0  # changing the element at the second row and second column to 0
print(matrix)

Output:

[[1, 2, 3], [4, 0, 6], [7, 8, 9]]


5. Matrix operations:
You can perform various matrix operations using nested loops or list comprehensions, such as addition, multiplication, etc. For example:

# Matrix addition
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
print(result)  # Output: [[6, 8], [10, 12]]

####TUPLE DATA STRUCTURE

#CREATION
1. Using parentheses:

my_tuple = (1, 2, 3, 4, 5)

2. Using the tuple() constructor:

my_tuple = tuple([1, 2, 3, 4, 5])


3. Creating an empty tuple:
python
empty_tuple = ()


4. Creating a tuple with a single element:
python
single_element_tuple = (1,)  
# Note the comma after the single element


5. Using a tuple literal:

another_tuple = 1, 2, 3, 4, 5

####ACCESSING TUPLE

my_tuple = (10, 20, 30, 40, 50)

# Accessing individual elements
first_element = my_tuple[0]
print(first_element)  # Output: 10

third_element = my_tuple[2]
print(third_element)  # Output: 30

# Accessing elements using negative indexing
last_element = my_tuple[-1]
print(last_element)  # Output: 50

second_last_element = my_tuple[-2]
print(second_last_element)  # Output: 40

my_tuple = (10, 20, 30, 40, 50)

# Slicing to access multiple elements
subset = my_tuple[1:4]
print(subset)  # Output: (20, 30, 40)

# Accessing elements with steps
elements_with_step = my_tuple[::2]
print(elements_with_step)  # Output: (10, 30, 50)

###FUNCTIONS
1. len(): Returns the number of elements in the tuple.
    python
    my_tuple = (1, 2, 3, 4, 5)
    length = len(my_tuple)
    print(length)  # Output: 5
    

2. count(): Returns the number of occurrences of a specified element in the tuple.
    python
    my_tuple = (1, 2, 2, 3, 2, 4)
    count = my_tuple.count(2)
    print(count)  # Output: 3
    

3. index(): Returns the index of the first occurrence of a specified element in the tuple.
    python
    my_tuple = (1, 2, 3, 4, 5)
    index = my_tuple.index(3)
    print(index)  # Output: 2 (index of element 3)
    

4. sorted(): Returns a new sorted list from the elements of the tuple.
    python
    my_tuple = (3, 1, 4, 1, 5, 9, 2)
    sorted_tuple = sorted(my_tuple)
    print(sorted_tuple)  # Output: [1, 1, 2, 3, 4, 5, 9]
    

5. min() and max(): Returns the smallest and largest elements in the tuple, respectively.
    python
    my_tuple = (3, 1, 4, 1, 5, 9, 2)
    min_value = min(my_tuple)
    max_value = max(my_tuple)
    print(min_value, max_value)  # Output: 1 9
    

6. Comparison (cmp()): 
There's no direct equivalent of the cmp() 
function in Python 3 for tuples. In Python 2, 
cmp() was used to compare two objects. 

In Python 3, you can use comparison operators like 
<, >, <=, >=, and == directly to compare
 tuples.

#CREATE SET  {}
# Example 1: Creating a set of numbers
number_set = {1, 2, 3, 4, 5}
print(number_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Creating a set of strings
string_set = {"apple", "banana", "orange", "kiwi"}
print(string_set)  # Output: {'banana', 'kiwi', 'apple', 'orange'}

# Example 3: Creating a set from a list (removes duplicates)
list_of_numbers = [1, 2, 3, 3, 4, 4, 5]
set_from_list = set(list_of_numbers)
print(set_from_list)  # Output: {1, 2, 3, 4, 5}

# Example 4: Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

###ACCESSING
# Example 1: Checking for membership
fruits = {"apple", "banana", "orange", "kiwi"}
# Using the 'in' operator to check if an element is in the set
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False

# Example 2: Iterating over elements
for i in fruits:
    print(i)

# Example 3: Using the 'in' operator with conditional statements
if "kiwi" in fruits:
    print("Kiwi is in the set.")
else:
    print("Kiwi is not in the set.")

# Example 4: Converting the set to a list or tuple for indexing (not recommended due to unordered nature)
# Note: This approach is not reliable as the order is not guaranteed in a set.
fruits_list = list(fruits)
print(fruits_list[0])  # Output: Randomly chosen element

# Example 5: Using the 'pop()' method to remove and return a random element
random_fruit = fruits.pop()
print("Randomly chosen fruit:", random_fruit)

# Example 6: Using the 'remove()' method to remove a specific element
fruits.remove("banana")
print(fruits)  # Output: {'orange', 'kiwi', 'apple'}


###SET FUNCTIONS
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.update({4, 5, 6})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3}
copied_set = my_set.copy()

my_set = {1, 2, 3}
popped_element = my_set.pop()

my_set = {1, 2, 3}
my_set.remove(2)

my_set = {1, 2, 3}
my_set.discard(2)

my_set = {1, 2, 3}
my_set.clear()
##MATHEMATICAL OPERATIONS
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: Returns a new set containing all unique elements from both sets
union_set = set1.union(set2)
print("Union:", union_set)  
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Returns a new set containing elements that are common to both sets
inter = set1.intersection(set2)
print(inter)  # Output: {4, 5}

# Difference: Returns a new set 
#containing elements that are present
 #in the first set but not in the second set
dif = set1.difference(set2)
print(dif)  # Output: {1, 2, 3}

# Symmetric Difference: Returns a new set containing elements that are present in either of the sets, but not in both
symm = set1.symmetric_difference(set2)
print(symmetric_difference_set)  
# Output: {1, 2, 3, 6, 7, 8}


'''DICTIONARY CREATION'''
# Example 1: Creating a dictionary with literal syntax
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Example 2: Creating a dictionary using the dict() constructor
another_dict = dict(name="Bob", age=25, city="Los Angeles")
print(another_dict)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# Example 3: Creating a dictionary from key-value pairs using zip() function
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Example 4: Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}


'''ACCESSING'''
my_dict = {"name": "Alice", "age": 30, 
"city": "New York"}

# Accessing value by key
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30


# Using the get() method
print(my_dict.get("city"))       # Output: New York
print(my_dict.get("gender"))     # Output: None
print(my_dict.get("gender", "Unknown"))  # Output: Unknown (with default value)

my_dict = {"name": "Alice", "age": 30, 
"city": "New York"}
# Iterating over keys
for key in my_dict:
    print(key, ":", my_dict[key])

# Using the items() method
for key, value in my_dict.items():
    print(key, ":", value)

'''FUNCTIONS'''
dict(): Creates a new dictionary. 
You can pass key-value pairs as arguments or pass an iterable of key-value pairs.

my_dict = 
dict(name="Alice", age=30, city="New York")

len(): Returns the number of items 
(key-value pairs) in the dictionary.

num_items = len(my_dict)

'''Methods:'''
clear(): Removes all items from the dictionary.
my_dict.clear()

get(): Returns the value for the specified key. 
If the key is not found, 
it returns a default value (None by default).
age = my_dict.get("age")

pop(): Removes the item with the specified key 
and returns its value. Raises a KeyError 
if the key is not found.
age = my_dict.pop("age")


popitem(): Removes and returns an arbitrary 
key-value pair from the dictionary as a tuple. 
Raises a KeyError if the dictionary is empty.
item = my_dict.popitem()

keys(): Returns a view object that displays a 
list of all the keys in the dictionary.
all_keys = my_dict.keys()

values(): Returns a view object that displays 
a list of all the values in the dictionary.
all_values = my_dict.values()


items(): Returns a view object that displays 
a list of all the key-value tuple pairs 
in the dictionary.
all_items = my_dict.items()


copy(): Returns a shallow copy of the dictionary.

copied_dict = my_dict.copy()


setdefault(): Returns the value of the 
specified key. If the key does not exist, 
inserts the key with a specified value 
(None by default).
age = my_dict.setdefault("age", 0)

update(): Updates the dictionary with 
the specified key-value pairs from another 
dictionary or iterable.

my_dict.update({"city": "Los Angeles", 
"gender": "female"})



'''built-in functions often used in 
functional programming paradigms.'''

1. map(function, iterable):
   - Applies the given function to each item 
   in the iterable (such as a list) and 
   returns a new iterator with the results.
   - It takes two parameters: a function 
   and an iterable.
   - The function parameter is the function 
   to apply to each item in the iterable.
   - The iterable parameter is a sequence 
   (like list, tuple, etc.) 
   whose items will be processed by the function.

   Example:
   python
   # Doubling each number in a list
   numbers = [1, 2, 3, 4, 5]
   doubled = map(lambda x: x * 2, numbers)
   print(list(doubled))  
   # Output: [2, 4, 6, 8, 10]
   

2. filter(function, iterable):
   - Filters the elements of an iterable based 
   on whether the function returns True or False.
   - It takes two parameters: a function and 
   an iterable.
   - The function parameter is a function 
   that returns True or False.
   - The iterable parameter is a sequence 
   whose elements are filtered based on the 
   function.

   Example:
   python
   # Filtering even numbers from a list
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   evens = filter(lambda x: x % 2 == 0, numbers)
   print(list(evens))  # Output: [2, 4, 6, 8, 10]
   

3. reduce(function, iterable [, initializer]):
   - Applies a rolling computation to sequential 
   pairs of values in an iterable.
   - It takes three parameters: a function, 
   an iterable, and an optional initializer.
   - The function parameter is a function 
   that takes two arguments and returns a 
   single value.
   - The iterable parameter is a sequence 
   of values to be reduced.
   - The initializer parameter is an optional 
   initial value for the reduction.

   Note: In Python 3, reduce() is no longer a built-in function and has been moved to the functools module.

   Example:
   python
   from functools import reduce
   
   # Summing all the numbers in a list
   numbers = [1, 2, 3, 4, 5]
   total = reduce(lambda x, y: x + y, numbers)
   print(total)  # Output: 15
   




































Graduate Aptitude Test in Engineering (GATE) 
exam - -ve marking , 
888/1000

Indian Oil Corporation Limited (IOCL)
Oil and Natural Gas Corporation (ONGC) 
National Thermal Power Corporation (NTPC) 
Bharat Heavy Electricals Limited (BHEL) -
Power Grid Corporation of India Limited 
(POWERGRID) 
Steel Authority of India Limited (SAIL)
Hindustan Petroleum Corporation Limited (HPCL) 
GAIL (India) Limited - 
Gas Authority of India Limited


8th pay commision - 1.5 lakhs, 




B.E 
firmware  - h/w & s/w
offer letter

TCS, INfy, hcl, cognizant , capgemini, ibm 
r1- aptitude test - R S Agarwal 
Quant - 
logical - 
verbal -

r2 - GD - THE HINDU 

r3 - civil / 71 programs 
r4 - hr round 



M. TECH 
GATE - SBI, CAnara, IOB , RBI, 
PGCET - 5 previous 

MS - GRE , TOFEL 

MBA - cat , gmat 

PSUs - RRB, RBI, 

ISRO - 
vssc - 
BARC - 
SSI 
MSI -
ADA -  
NAL - 



















#importing one module into another:

#Creating a Module:
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
    
1. Using import Statement:
import my_module

print(my_module.greet("Alice"))
print(my_module.add(5, 3))

2. Using from...import Statement:

from my_module import greet, add
print(greet("Bob"))
print(add(7, 2))


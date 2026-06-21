'basic concepts in Python'

#identation
"""
 a white space before a statement in a line of code. 
It is used to indicate that the statement is part of a block of code, such as a function or a loop. 
In Python, indentation is typically done using four spaces, but it can also be done using tabs. 
Proper indentation is important for the readability and structure of the code.  

# Example of indentation in Python
a=5
if a>0:
    print("happy birthday")
"""

#variables
"""
it is used to stores a values like a container but it is case sesitive
and in python, it is a dynamic typing.-we dont have to declare a daata type infront of variable..
"""

#comments
""" 
it igonores code and it is used to explain the code.
it has single comments and multi line comments.
single line comments are denoted by a hash symbol (#) and multi line comments are denoted by triple quotes ''' or """


#fundamental data types
"""
1. int: represents whole numbers, such as 1, 2, 3,
2. float: represents decimal numbers, such as 1.5, 2.0, 3.14,
3. str: represents a sequence of characters, such as "hello", 'world',
4. bool: represents a boolean value, which can be either True or False,
"""
# advanced data types:or data structures
"""
5. list: represents a collection of items, such as [1, 2, 3], ["apple", "banana", "cherry"],
6. tuple: represents an ordered, immutable collection of items, such as (1, 2, 3), ("apple", "banana", "cherry"),
7. dict: represents a collection of key-value pairs, such as {"name": "Alice", "age": 30},
8. set: represents an unordered collection of unique items, such as {1, 2, 3}, {"apple", "banana", "cherry"},

9. None: represents the absence of a value or a null value.
"""
"""
#operators
a=20
b=15

#arithmetic operators 
#it is used to perform arthimetic operations using operands
print("arithmetic operators")
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division 
print(a//b) #floor division = division that rounds down to the nearest whole number
print(a%b) #modulus  = remainder of a divided by b
print(a**b) #exponentiation = a power b

#assignment opeartors 
# (=, +=, -=, *=, /=, //=, %=, **=)
#it is used to assign values to variables

c=10 #assigns the value 10 to variable c
print("assignment operators")
print("c+=5", c) # c=c+5
print("c-=3", c) # c=c-3
print("c*=2", c) # c=c*2
print("c/=4", c) # c=c/4
print("c//=2", c) # c=c//2
print("c%=3", c) # c=c%3
print("c**=2", c) # c=c**2

#comparison operators
#it is used to compare two values and return a boolean result (either true or false)

d=100
e=200

print("comparison operators")
print(d==e) # equal to
print(e!=d) # not equal to
print(e>d) # greater than
print(e<d) # less than
print(e>=d) # greater than or equal to
print(e<=d) # less than or equal to

"""


#logical operators
"""
and, or, not
and"both operands are condition is true then it return true
"or"if at least one operand is true then it return true
"not"it is used to reverse the logical state of its operand.
     if a condition is true then it return false and if a condition is false then it return true
"""

#input function
"""
it used to take the input values from user .
by deault it returns string value.
if we want to take input as integer or float then we have to use int() or float() function to convert the string value into integer or float.

a=input("enter your name: ") #string value
b=int(input("enter your age: ")) #integer value
print("your name is", a)
print("your age is", b)
print(type(a))
print(type(b))


#module 1
#data types
name= "sanjay dharmireddi "
print(name)
print(type(name))

age =20
print(age)
print(type(age))

#variables
#swap
a=10
b=5
a,b=b,a
print(a)
print(b)

x=15
y=30
print("sum is ",x+y)

#operators
x=25
y=20
if x>y:
    print("x is greater than y")
else:
    print("y is greater than x")

x=25
if x%2==0:
    print("x is even")
else:
    print("x is odd")

#arthmetic operators
a=25
print(a**2) #square of a

radius=5
area=3.14159* radius**2
print(area)

#type conversion
a="100"
b=int(a) #string to integer
print(b)
print(type(b))

#Logical operators
age=eval(input("enter your age : "))
has_License=input("do u have license(true/false) : ")
has_License=has_License.lower()
if age>18 and has_License=="true" or has_License=="True":
    print("you can drive")
else:
    print("cannot drive")

#relational operators
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if num1>num2:
    print("num1 is greater than num2")
elif num1==num2:
    print("num1 and num2 are equal")
else:
    print("num 2 is greater than num1")

#assignment operators
count=10
count+=5
print(count)

#type conversion
price=19.99
print(int(price)) #float to integer
"""
pow()
    
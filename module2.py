#conditional statements
"""
if condition:
    #code to be executed if condition is true
elif condition2:
    #code to be executed if condition2 is true
else:
    #code to be executed if both conditions are false

a=24
b=24
if a<b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

"""

#nested if
"""
age=20
if age>=18:
    print("you are eligible to vote")
    if age>=21:
        print("you are eligible for driving license")
    else:
        print("you are not eligible for driving license")
else:
    print("you are not eligible to vote")
"""

#loops
"""
for loop and while loop:
for loop is used to when iteration is know (we know when the condition is false)
while loop is used when iteration is not know (we dont know when the condition is false)

for loop syntax:
for variable in sequence:
    #code to be executed for each item in sequence

while loop syntax:
while condition:
    #code to be executed as long as condition is true
"""
"""
#for loop
for i in "hello":
    print(i)




for i in range(1,11):
    print(i)



#while loop
i = 0
while i <= 10:
    print(i)
    i+=1


password=""
while password.lower()!="sanjay":
    password=input("enter password:")

"""
"""
#break and continue
#break is used to exit the loop when a certain condition is met
#continue is used to skip the current iteration and move to the next iteration when a certain condition is met.

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

"""

#functions
#a function is block of code which only runs when it called.
#we can pass data into a function through parameters or arguments and it can return data as a result..
def add(a1,b1):
    c=a1+b1
    print(f"The sum of {a1} and {b1} is {c}")
    return c
    

a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
add(a,b)

def add(a, b):
    a+b
    return a+b

result = add(10, 20)

print(result)
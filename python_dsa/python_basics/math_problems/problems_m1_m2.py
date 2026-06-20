"""
1 Check if a number is even (try for odd number).
2 Print n natural number using for loop and while loop
3 Print any input string n Times using loops
4 print each character from the given string
5 Check if two strings are anagrams. (for loop)
6 Reverse a string using slicing.
7 Check if a string is a palindrome.
8 reverse a given number
9 Print multiplication table for given number
10 swap two numbers without using a temporary variables
11 Calculate the factorial of a number. (while loop)
12 Find the maximum and minimum of three numbers.
13 print sum of n natural numbers (while loop)
"""

"""
#check if a number is even(try for odd number).
num=eval(input("Enter a number : "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

"""

"""
#print n natural numbers using for loop
numbers=int(input("enter how many number u want : "))
for i in range(1,numbers+1):
    print(i)

#print n natural numbers using while loop
num=int(input("enter how many natural u want :  "))
i=1
while i<=num:
    print(i)
    i+=1
   
"""


"""
#print any input string n times using loops
n=int(input("how many string u want : "))
strings=[]
for i in range(1,n+1):
    word=input(f" Enter string {i} : ")
    strings.append(word)
print(strings)


number=int(input("how many strings u want : "))
stringswhile=[]
i=1
while i<=number:
    word=input(f" Enter string {i} : ")
    stringswhile.append(word)
    i+=1
print(stringswhile)

"""
"""
#print each character from string
user=input(" Enter string : ")
for i in user:
    print(i)

"""

"""
#check if two strings are anagram or not.
user1=input(" Enter string 1 : ")
user2=input("Enter string 2 : ")
anagram=""
if len(user1)==len(user2):
    for i in user1:
        if i in user2:
            anagram="strings are anagram"
        else:
            anagram="strings are not anagram"
else:
    print("strings are not anagram")
print(anagram)

"""
"""
#reverse a string using slicing
string=input("enter a string : ")
print(string[::-1])
"""
"""
#check if a number or string is palindrome
user_input=input("Enter number or string : ")
if user_input==user_input[::-1]:
    print("number or string is palindrome")
else:
    print("number or string not a palindrome")

"""
"""
#reverse a number
number=int(input("Enter number : "))
if str(number)[0]=="-":
    number1="-"+ str(number)[:0:-1]
    print(int(number1))
else:
     print(int(str(number)[::-1]))
"""

"""
#print multiplication number for user input number
user_input=int(input("Enter a number for multiplication table : "))
for i in range(1,13):
    print(f"{user_input} * {i} = ",i*user_input)
"""
"""
#swap two number without using temporary variable
number1=int(input("Enter number 1 : "))
number2=int(input("Enter number 2 : "))
number1,number2=number2,number1
print(f"swap of two numbers : {number1} , {number2} ")
"""
"""
#calculate a factorial using while loop
n=int(input("enter factorial number u want : "))
result=1
while n>1:
    result=result*n
    n=n-1
print("factorial number : ",result)
"""

"""
#find the maximum and minimum of three numbers
num=int(input("How many number u want : "))
compare=[]
for i in range(1,num+1):
    num1=int(input(f"Enter {i} number: "))
    compare.append(num1)
    max=compare[0]
    mini=compare[0]
    for j in compare:
        if j>max:
            max=j
        else:
            mini=j
print("maximum number is : ",max)
print("minimum number is : ",mini)
print(type(max))

"""
"""
#print sum of n naturl numbers using while loop
n=int(input("how many numbers u want to add natural numbers : "))
num=n
result=0
i=1
while n>0:
    result+=n
    n-=1
print(f"sum of {num} natural numbers is : ",result)
"""
"""
user={}
while True:
    keys=input("enter key : ")
    if keys=="00":
        break
    value=input("enter values : ")
    user[keys]=value

print(user)


emp={}
while True:
    keys=input("Enter key : ")
    value=input("enter value : ")
    emp[keys]=value
    if len(emp)==4:
        break
print(emp)

"""
"""
1. Consecutive Character Compression

Input:

aaabbccccdd

Output:

a3b2c4d2

Explanation:

aaa -> a3
bb -> b2
cccc -> c4
dd -> d2

s = "aaabbccccdd"
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1
print(s[-1] + str(count))
"""

sentence=input("Enter sentence : ")
words=sentence.split()

print("total words : ",len(words))
print("number of unique words : ",len(set(words)))
common=[]

print("\n",words)
for i in range(len(words)):
        for j in range(i,len(words)):
            word1=words[i]
            word2=words[j]
            if len(word1)>len(word2):
                long=word1
            if len(word1)<len(word2):
                short=word1
            if len(word1)==len(word2):
                common.extend([word1,word2])
                 
print("long :",long)
print("short :",short)
    


"""
Pattern 1 — Square Star Pattern

****
****
****
****


for i in range(4):
    for j in range(4):
        print(" * ",end="")
    print()

Pattern 2 — right angle triangle Pattern

*
**
***
****


for i in range(0,4):
    for j in range(0,i+1):
        print(" * ",end="")
    print()

    
3. Number Triangle

1
12
123
1234
12345


count=1
for i in range(0,5):
    for j in range(0,i+1):
        print(j+1,end="")
    print()

4. Same Number Triangle

1
22
333
4444
55555



count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

    
Pattern 5 — Inverted Triangle


* * * * *
* * * *
* * *
* *
*



for i in range(0,5):
    for j in range(0,5-i):
        print(" * ",end="")
    print()

    
Pattern 6 — Continuous Numbers

For n = 5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15



count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end="")
        count+=1
    print()

    
Pattern 7 — Reverse Number Triangle

For n = 5

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


for i in range (1,6):
    for j in range(1,7-i):
        print(j,end="")
    print()

    
Pattern 8 — Alphabet Triangle

For n = 5

A
A B
A B C
A B C D
A B C D E

for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+j),end="")
    print()

    
Pattern 9 — Same Alphabet Triangle
A
B B
C C C
D D D D
E E E E E


for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+i),end="")
    print()


Pattern 10 — Pyramid

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


n=5
for i in range(n):
    for j in range(1,i):
        space=" "*n-i
        star=" *"*j
        print(space, star,end="")
    print()


n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


n=5
for i in range(1,n+1):
    for j in range(1, i):
        print(" ",end="")
    for j in range(0, n-i+1):
        print("*",end="")
    print()

hill pattern
n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

Pattern 11 — Inverted Pyramid
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *    


n=5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,n-i):
        print("*",end="")
    for j in range(1,n-i):
        print("*",end="")
    print()

Pattern 12 — Diamond
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *


n=5
for i in range(n):
    for j in range(1,n-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

k=4
for i in range(k):
    for j in range(0,i+1):
        print(" ",end="")
    for j in range(0,k-i):
        print("*",end="")
    for j in range(1,k-i):
        print("*",end="")
    print()
    

Pattern 13 — Hollow Square
* * * * *
*       *
*       *
*       *
* * * * *



n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

    
Pattern 14 — Hollow Triangle
*
* *
*   *
*     *
* * * * *


n=5
for i in range(n):
    for j in range(0,i+1):
        if i==0 or j==0 or i==j or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

    
Pattern 15 — Floyd's Triangle
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15


n=5
count=1
for i in range(n):
    for j in range(0,i+1):
        print(" ",count,end="")
        count+=1
    print()

    
Pattern 16 — Binary Triangle
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1



n=5
for i in range(n):
    for j in range(0,i+1):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()

    
Pattern 17 — Multiplication Triangle
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25

"""
n=5
count=1
for i in range(n):
    for j in range(1,i+1):
        print(" ",count,end="")
        count*=j
    print()
        



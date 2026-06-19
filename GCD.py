"""
GCD of Two Numbers
Subscribe to TUF+

Hints
Company
You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Example 1

Input: n1 = 4, n2 = 6

Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6

Greatest Common divisor = 2.

Example 2

Input: n1 = 9, n2 = 8

Output: 1

Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.

Greatest Common divisor = 1.

Now your turn!

Input: n1 = 6, n2 = 12

Output:


Validate

12

6

1

9
Constraints

1 <= n1, n2 <= 1000
"""
n1=int(input("Enter 1st number : "))
n2=int(input("Enter second number : "))
small=min(n1,n2)
gcd=1
for i in range(1, small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print("GCD is : ",gcd)


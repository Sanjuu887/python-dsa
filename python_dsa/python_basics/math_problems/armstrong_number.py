"""
Check if a number is Armstrong Number or not


18

Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
Examples
Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371
"""

def isArmstrong(n):
        subn=n
        final=n
        count=0
        arm=0

        while n>0:
            n=n//10
            count+=1

        while subn>0:
            su=subn%10
            arm+=su**count
            subn=subn//10

        if arm==final:
            tru="true"
            return tru
        else:
            fal="false"
            return fal

n=int(input("Enter number : "))
ans=isArmstrong(n)
print(ans)
        

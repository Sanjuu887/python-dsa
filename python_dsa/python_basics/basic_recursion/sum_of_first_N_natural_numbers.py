"""
Sum of first N Natural Numbers

Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

Examples
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
"""

def numbers(n,i,sum):
    if n<=0:
        return sum
    n-=1 
    i+=1 
    sum+=i 
    return numbers(n,i,sum) 
    

n=int(input("enter n value : "))
i=0
sum=0
ans=numbers(n,i,sum)
print(f"sum of {n} natural numbers : ",ans)
"""
Print Name N times using Recursion

Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
"""

def n_time(name,repeat):
    if repeat<=0:
        return
    print(name,end=" ")
    repeat-=1
    n_time(name,repeat)

name=input("Enter name : ")
repeat=int(input("Enter how times u want to repeat : "))

n_time(name,repeat)
 

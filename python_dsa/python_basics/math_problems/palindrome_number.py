"""
Check if a number is Palindrome or Not

Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.
"""

n=int(input("enter number : "))
org=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==org:
    print("Palindrome Number")
else:
    print("Not Palindrome")
    
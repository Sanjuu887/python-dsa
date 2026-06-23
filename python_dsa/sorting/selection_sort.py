"""
Selection Sort Algorithm

Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Examples
Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5

"""

n=int(input("Enter number elements you want : "))
li=[]
for i in range(n):
    elements=int(input("enter elements : "))
    li.append(elements)

for i in range(n):
    min=i
    for j in range(i,n):
        if li[j]<li[min]:
            min=j
            
    li[min],li[i]=li[i],li[min]
print(li)
        



"""
Bubble Sort Algorithm

Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

Examples

Example 1:
Input: N = 5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting we get 1,2,3,4,5


Example 2:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
            
"""

n = int(input("Enter number of elements: "))

li = []
for i in range(n):
    ele = int(input("enter element: "))
    li.append(ele)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("sorted List:", li)
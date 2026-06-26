"""
Insertion Sort Algorithm

Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.

A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

Examples
Example 1:
Input:
  nums = [7, 4, 1, 5, 3]  
Output:
  [1, 3, 4, 5, 7]  
Explanation:
  The array is sorted in non-decreasing order: 1 ≤ 3 ≤ 4 ≤ 5 ≤ 7.

Example 2:
Input:
  nums = [5, 4, 4, 1, 1]  
Output:
  [1, 1, 4, 4, 5]  
Explanation:
  The array is sorted in non-decreasing order: 1 ≤ 1 ≤ 4 ≤ 4 ≤ 5.
  
"""

n = int(input("Enter number of elements: "))

li = []
for i in range(n):
    ele = int(input("Enter element: "))
    li.append(ele)

for i in range(1, n):
    key = li[i]
    j = i - 1

    while j >= 0 and li[j] > key:
        li[j + 1] = li[j]
        j -= 1

    li[j + 1] = key

print("sorted list:", li)
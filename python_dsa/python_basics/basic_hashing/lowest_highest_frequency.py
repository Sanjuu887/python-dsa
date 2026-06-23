"""
Find the highest/lowest frequency element

Problem Statement: Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

Examples
Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.


Example 2:
Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.
            
            
"""


n=int(input("Enter number of elements : "))
li=[]
for i in range(n):
    ele=int(input("Enter element : "))
    li.append(ele)

frequency={}
for i in li:
    #frequency[i]=frequency.get(i,0)+1 #1st option
    if i in frequency:   #2nd option
        frequency[i]+=1
    else:
        frequency[i]=1
        
max_key=0
min_key=0
max_val=0
min_val=6

for key,value in frequency.items():
    if value>max_val:
        max_val=value
        max_key=key
    if value<min_val:
        min_val=value
        min_key=key
print("highest frequency of element is : ",max_key," frequency is : ",max_val)
print("lowest frequency of element is : ",min_key," frequency is : ",min_val)
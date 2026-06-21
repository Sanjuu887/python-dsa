"""
Reverse a given Array

Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

"""
def reverse(array_elements,left, right):
    if left>=right:
        return array_elements
    array_elements[left], array_elements[right]=array_elements[right], array_elements[left]
    left+=1
    right-=1
    return reverse(array_elements,left, right)

n=int(input("Enter number of elements : "))
array_elements=[]
left=0
right=n-1

for i in range(n):
    elements=int(input("enter element : "))
    array_elements.append(elements)

print("orginal array : ",array_elements)
print("reverse array : ",reverse(array_elements,left, right))


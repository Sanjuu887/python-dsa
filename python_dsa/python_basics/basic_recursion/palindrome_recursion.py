"""
Check if the given String is Palindrome or not

Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

Examples
Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.

"""
def palindrome(str_array,left,right):
    if left>=right:
        return "".join(str_array)
    str_array[left],str_array[right]=str_array[right],str_array[left]
    left+=1
    right-=1
    return palindrome(str_array,left,right)


str=input("enter string : ")
left=0
right=len(str)-1
str_array=[]

for i in str:
    str_array.append(i)

if str==palindrome(str_array,left,right):
    print("palindrome")
else:
    print("not palindrome")



"""
Problem 1 — Student Marks Report

You are given marks of 5 students in a list.

Example:

marks = [45, 67, 89, 32, 76]

Each number represents marks of one student.

Example:

45 → Student 1 marks
67 → Student 2 marks
and so on...

Your task is to write a program that:

Prints total marks of all students combined
Prints average marks
Prints highest marks
Prints lowest marks
Prints number of students passed

Condition:

Student passes if marks are greater than or equal to 35

Expected thinking:

Use loops
Use conditions
Use variables for tracking values
Build logic manually

Don’t use advanced shortcuts like:

sum()
max()
min()

First build logic yourself.

Try solving fully first.
"""

marks = [43, 32, 24, 67, 81]

total = 0
passed = 0

highest = marks[0]
lowest = marks[0]

# total, highest, lowest, passed students
for i in marks:

    total += i

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

    if i >= 35:
        passed += 1

# average
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Passed Students:", passed)

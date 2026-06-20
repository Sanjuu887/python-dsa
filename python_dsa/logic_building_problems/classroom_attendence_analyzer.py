"""
Problem 5 — Classroom Attendance Analyzer
Scenario

A college has two groups of students:

Classroom Students
{"Sanjay", "Rahul", "Ravi", "Kiran", "Aman"}
Sports Participants
{"Rahul", "Kiran", "Aman", "Arjun"}
Requirements

Print the following:

1. Students who belong to BOTH groups

Output example:

Rahul
Kiran
Aman
2. Students who belong ONLY to Classroom

Output example:

Sanjay
Ravi
3. Students who belong ONLY to Sports

Output example:

Arjun
4. Total Unique Students

Output example:

Total Unique Students : 6
5. Student Search

Ask user:

Enter Student Name:
Rules
Case 1

If student is present in BOTH groups:

Example Input:

Rahul

Output:

Present in Classroom and Sports
Case 2

If student is present ONLY in Classroom:

Example Input:

Sanjay

Output:

Present only in Classroom
Case 3

If student is present ONLY in Sports:

Example Input:

Arjun

Output:

Present only in Sports
Case 4

If student does not exist in either group:

Example Input:

Vijay

Output:

Student Not Found
Additional Rule

Search should not be case-sensitive.

Example:

Input:

rahul

Output:

Present in Classroom and Sports
Topics Covered

✅ Sets
✅ Set Operations
✅ Membership Checking (in)
✅ Conditions
✅ User Input
✅ String Handling (lower())

Difficulty

🟠 Medium-Hard

Before writing code, answer these 2 questions mentally:
1. Which data structure is perfect for this problem?

and

2. What operation gives common students?
"""

print("..Aditya university..\n")

classroom={"sanjay","rahul","ravi","kiran","aman"}
sports={"rahul","kiran","aman","arjun"}

both_groups=classroom.intersection(sports)
only_classroom=classroom.difference(sports)
only_sports=sports.difference(classroom)
unique=classroom.union(sports)
print("students are present in Both classroom and sports : \n",both_groups)

print("students are present in classroom:  ",only_classroom)

print("students are present in sports : \n",only_sports)

print("Total unique students are present in Both classroom and sports : \n",len(unique))
print(unique)

students=input("enter student name : ")
students=students.lower()

while len(students)==0:
    print("Empty, pls enter correct name ..")
    students=input("enter student name : ")
    if len(students)!=0:
        break

if students in both_groups:
    print(students,"is present in both classroom and sports")
elif students in only_classroom:
    print(students,"is present only in classroom")
elif students in only_sports:
    print(students,"is present only in sports")
else:
    print(students,"is not found")

    

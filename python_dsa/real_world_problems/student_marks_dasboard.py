"""
Problem 7 — Student Marks Dashboard
Scenario

You are building a college student management dashboard.

The system should store student details and perform analysis.

Requirements

Ask user:

How many students?

For each student collect:

Roll Number
Student Name
Marks
Validation Rules
Rule 1

Roll Number must be unique.

Example:

101
101

Output:

Roll Number Already Exists

Ask again.

Rule 2

Marks must be between:

0 to 100

Example:

120

Output:

Invalid Marks

Ask again.

After Storing All Students

Print:

1. Highest Scorer

Example:

Highest Scorer

Roll Number : 101
Name : Sanjay
Marks : 95
2. Lowest Scorer

Example:

Lowest Scorer

Roll Number : 104
Name : Ravi
Marks : 22
3. Average Marks

Example:

Average Marks : 68.75
4. Pass Count

Pass Marks:

35

Example:

Passed Students : 4
5. Fail Count

Example:

Failed Students : 1
6. Distinction Count

Distinction:

Marks >= 75

Example:

Distinction Students : 2
7. Search Student

Ask:

Enter Roll Number:

If found:

Student Found

Roll Number : 101
Name : Sanjay
Marks : 95

If not found:

Student Not Found
Sample Input
3

101
Sanjay
95

102
Rahul
70

103
Ravi
25
Expected Output
Highest Scorer
101
Sanjay
95

Lowest Scorer
103
Ravi
25

Average Marks : 63.33

Passed Students : 2

Failed Students : 1

Distinction Students : 1
What This Problem Tests

✅ Dictionaries

✅ Nested Dictionaries

✅ Validation

✅ Searching

✅ Highest/Lowest Pattern

✅ Average Calculation

✅ Real-world Data Storage
"""

students={}
student_records={}

number=int(input("how many students records do u want to store : "))

while number>0:
    roll=input("Enter student roll number : ")
    if roll in students:
        print("student roll number is already exist..")
        roll=input("Enter student roll number : ")
    else:
        name=input("Enter student name : ")
        marks=int(input("Enter marks : "))
        while True:
            if marks<0 or marks>100:
                print("..Invalid marks..")
                marks=int(input("Enter marks : "))
            else:
                break
    students[roll]={
            "name": name,
            "marks": marks
        }
    number-=1

rolls=list(students.keys())

highest=rolls[0]
lowest=rolls[0]
total=0
passcount=0
fail=0
distinction=0

for curr in rolls:
    if students[curr]["marks"]>students[highest]["marks"]:
        highest=curr
    if students[curr]["marks"]<students[lowest]["marks"]:
        lowest=curr
    total+=students[curr]["marks"]
    if students[curr]["marks"]>=35:
        passcount+=1
    if students[curr]["marks"]<35:
        fail+=1
    if students[curr]["marks"]>=75:
        distinction+=1

print("\n..highest scorer ..\n",students.get(highest))
print("\n..lowest scorer ..\n",students.get(lowest))
print("\naverage marks : ",total/len(students))
print("\nTotal students pass count :  ",passcount)
print("\nTotal students Fail count :  ",fail)
print("\nTotal students distinction count :  ",distinction)


search=input("\nEnter roll number to search : ")
if search in students:
    print("\n",students[search])
else:
    print("\nStudent not found")




    
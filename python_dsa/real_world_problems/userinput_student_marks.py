"""
2. Student Result Management System

Take marks of 5 students from user using loop.

After entering all marks:
Print:

total marks
average
highest marks
lowest marks
failed students count

Rules:

fail if marks < 35
distinction if marks >= 75

Also print:

Number of distinction students
"""
students=int(input("Enter how many students : "))
marks=[]
total=0
passcount=0
distinctionpass=0
failed=0
for i in range(students):
    marks.append(int(input(f"Enter student {i+1} marks : ")))
print(marks)
highest=marks[0]
lowest=marks[0]
for j in marks:
    total+=j
    if j>=highest:
        highest=j
    if lowest>=j:
        lowest=j
    if j<35:
        failed+=1
    if j>=35 and j<=100:
         passcount+=1
    if j>=75:
        distinctionpass+=1
    else:
        pass


avg=total/students

print("Total students marks :",total)
print("Average marks : ", avg)
print("highest marks : ",highest)
print("lowest marks : ",lowest)
print("total destinction students :",distinctionpass)
print("total passed students :",passcount)
print("Total failed students : ",failed)
    
    

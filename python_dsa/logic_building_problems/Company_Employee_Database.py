"""
Problem 2 — Company Employee Database
Scenario

A company wants to store employee records.

Each employee has:

Employee ID
Employee Name
Department
Salary
Requirements

The program should:

Step 1

Ask:

How many employees do you want to store?
Step 2

Take details of each employee:

Employee ID
Employee Name
Department
Salary

Store all employee records.

Step 3

After storing all records,

ask user:

Enter Employee ID to Search:
Step 4

If Employee ID exists,

print:

Employee ID
Employee Name
Department
Salary
Step 5

If Employee ID does not exist,

print:

Employee Not Found
Rules
Rule 1

Employee IDs must be unique.

If a user enters an already existing Employee ID:

Employee ID Already Exists

Ask again.

Rule 2

Salary cannot be negative.

If negative salary entered:

Invalid Salary

Ask again.

Rule 3

Department name should not be empty.

If empty:

Department Cannot Be Empty

Ask again.

Example Test Case 1
Number of Employees: 2

ID: 101
Name: Sanjay
Department: AI
Salary: 25000

ID: 102
Name: Rahul
Department: Data Science
Salary: 30000

Search:

Enter Employee ID: 101

Output:

Employee ID: 101
Name: Sanjay
Department: AI
Salary: 25000
Example Test Case 2

Search:

Enter Employee ID: 999

Output:

Employee Not Found
Topics Covered

✅ Dictionaries
✅ Nested Dictionaries
✅ Loops
✅ Conditions
✅ Input Validation
✅ Search Operations

"""

employees = {}

num = int(input("How many employees do you want to store? : "))

for i in range(num):

    print(f"\nEmployee {i+1}")

    while True:
        emp_id = input("Enter Employee ID: ")

        if emp_id not in employees:
            break

        print("Employee ID Already Exists")

    name = input("Enter Employee Name: ")

    while True:
        department = input("Enter Department: ")

        if department != "":
            break

        print("Department Cannot Be Empty")

    while True:
        salary = int(input("Enter Salary: "))

        if salary >= 0:
            break

        print("Invalid Salary")

    employees[emp_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }

print("\nStored Employee Records Successfully")

search_id = input("\nEnter Employee ID to Search: ")

if search_id in employees:

    print("\nEmployee Found")

    print("Employee ID :", search_id)
    print("Name :", employees[search_id]["name"])
    print("Department :", employees[search_id]["department"])
    print("Salary :", employees[search_id]["salary"])

else:
    print("Employee Not Found")
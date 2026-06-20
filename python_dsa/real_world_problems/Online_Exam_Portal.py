"""
Problem 1 — Online Exam Portal
Scenario

A student attends an online exam.

The exam contains:

10 Questions

Each question carries equal marks.

Requirements

The program should ask the student:

How many questions did you answer correctly?
Rules
Rule 1

The number of correct answers cannot be:

Less than 0
More than 10

If user enters an invalid number:

Invalid Input

and ask again.

Rule 2

After a valid input is entered:

Print:

Total Score
Rule 3

Print:

Percentage
Rule 4

Print Result:

Pass

or

Fail
Rule 5

Print Grade:

A
B
C
D
F

according to the student's performance.

Example Test Case 1
Enter Correct Answers: 8

Output:

Total Score: ?
Percentage: ?
Result: Pass
Grade: ?
Example Test Case 2
Enter Correct Answers: 3

Output:

Total Score: ?
Percentage: ?
Result: Fail
Grade: ?
Example Test Case 3
Enter Correct Answers: 15

Output:

Invalid Input

and ask again.
"""
def exam_questions():
    questions=int(input("Enter how many questions did u answer correctly : "))
    return questions

def total_score(questions):
    score=questions*10
    return score
    

def percentage(total):
    percentage=(total/100)*100
    print("Percentage is : ",percentage)

def result(total):
    if total>=40:
        results="Pass"
        return results
    else:
        results="Fail"
        return results


def Grade(total):
    if total>=40 and total<50:
        print("Grade : E")
    elif total>=50 and total<60:
        print("Grade : D")
    elif total>=60 and total<70:
        print("Grade : C")
    elif total>=70 and total<80:
        print("Grade : B")
    elif total>=80 and total<90:
        print("Grade : A")
    elif total>=90 and total<100:
        print("Grade : A+")
    elif total==100:
        print("Grade : S")
    else:
        print("Grade : F")

def validate():
    print(" ")
    key=input("Enter into portal again yes(any key) no (00): ")
    return key

while True:
    print(" ")
    print("Online Exam portal")
    print(" ")
    questions=exam_questions()
    if questions>=0 and questions<=10:
        total=total_score(questions)
        print("Total marks : ",total)

        percentage(total)

        resulting=result(total)
        print("result : ",resulting)

        Grade(total)
    else:
        print("...Invalid Input...")
    
    
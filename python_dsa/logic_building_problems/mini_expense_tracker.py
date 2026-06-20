"""
Problem 6 — Mini Expense Tracker

Your program should repeatedly ask user:

Enter expense amount:
Conditions
Case 1 — Valid Expense

If user enters positive amount:

add it to total expenses
Case 2 — Stop Program

If user enters:

done

Program should stop taking inputs.

After stopping, print:
Total expenses
Highest expense
Lowest expense
Average expense
Number of expenses entered
Case 3 — Invalid Expense

If user enters:

0 or negative amount

Print:

Invalid expense amount

and ask again.

Example Flow
Enter expense amount: 200
Enter expense amount: 500
Enter expense amount: -30
Invalid expense amount
Enter expense amount: 100
Enter expense amount: done

Then print final report.

Important

Do manually.
Don’t use:

sum()
max()
min()

Build logic yourself using:

loops
conditions
variables
tracking patterns.
"""
total=0
all=[]
user_input1=1
number=0
while user_input1!="done" and user_input1!="DONE":
    print(" ")
    expense=int(input("enter expenses :"))
    total+=expense
    number+=1
    all.append(expense)
    if expense<0:
        print("invalid input")
    user_input1=input("do u want to enter again : if yes(any key) no(type : done): ")
print(" ")
print("list of all expenses : ", all)
high=all[0]
low=all[0]
avg=0
print(" ")
print("Total expenses ",total)
for i in all:
    if i>=high:
        high=i
    if i<=low:
        low=i

avg=(total/number)
print(" ")
print("highest expense : ",high)
print(" ")
print("lowest  expense: ",low)
print(" ")
print("average of all expenses: ",avg)
print(" ")
print("Total number of entries : ",number)





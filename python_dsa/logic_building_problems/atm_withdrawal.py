"""
Problem 2 — ATM Withdrawal System

You are building a simple ATM program.

Initial account balance:

balance = 10000

Your program should:

Ask the user to enter withdrawal amount
Check:
if amount is less than or equal to balance → allow withdrawal
otherwise → print "Insufficient Balance"
After successful withdrawal:
subtract amount from balance
print remaining balance
Program should keep running again and again until user enters:
0

If user enters 0, print:

Thank you for using ATM

and stop program.

Conditions:

Use loops
Use conditions
Don’t use advanced concepts
Think like a real ATM flow


"""

initial_amount=10000
while True:
    amount_withdrawal=int(input("Enter the amount to withdrawal : "))
    while amount_withdrawal<0:
        print("please enter correct amount")
        amount_withdrawal=int(input("Enter the amount to withdrawal : "))
            
    if amount_withdrawal==0 :
        print("Thank you for using ATM")
        break
    if amount_withdrawal<=initial_amount:
        print(" ")
        print("Actual Balance : ", initial_amount)
        print(f"{amount_withdrawal} : amount withdrawal")

        remaining_balance=initial_amount-amount_withdrawal
        print(" ")

        print("Remaining balance is : ",remaining_balance)
        initial_amount=remaining_balance
        print(" ")
    else:
        print(" ")
        print("Insufficient balance")
        print("current Balance :  ",initial_amount)





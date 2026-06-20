"""
1. Mobile Recharge System

Initial balance:

balance = 500

Recharge plans:

199
399
599

Program should:

ask user to choose plan
check if enough balance exists
deduct amount
print remaining balance
keep running until user enters:
exit

Invalid plan:

Invalid Recharge Plan
"""
print("Mobile Recharge System")
print(" ")
balance=500
user_input1=1
while user_input1!=0:
    print("Choose the available mobile recharge plans : (199, 399, 599)")
    user_input=int(input("Enter the selected plan here : "))
    if user_input == 199 or user_input==399 or user_input==599 :
        print(f"you selected {user_input} plan..")
        if balance<=0:
            print("Insuffiecient balance")
        elif user_input<balance:
            print("Recharge successfull...!!")
            balance-=user_input
            print("current balance : ",balance)
            print(" ") 
        else:
            print("Insuffiecient Balance")
            print("current balance : ",balance)
        
        
    else:
        print("Invalid recharge plan")
    print(" ")
    print("Do You want to continue (yes 0)(no - any key)")
    user_input1=input("Enter your choice:")
    str(user_input1)
        
    break
print("Thank u for choosing us")
            







































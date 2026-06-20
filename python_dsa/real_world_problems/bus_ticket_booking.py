"""
Problem 5 — Bus Ticket Booking System

A bus has:

40 seats

Your program should repeatedly ask the user:

How many tickets do you want to book?
Conditions
Case 1 — Valid Booking

If requested tickets are less than or equal to available seats:

booking should succeed
reduce available seats
print remaining seats

Example:

Tickets Booked Successfully
Remaining Seats: 25
Case 2 — Overbooking

If requested tickets are greater than available seats:
Print:

Only X seats available

Example:

Only 5 seats available

Do NOT reduce seats.

Case 3 — Invalid Input

If user enters:

0 or negative number

Print:

Invalid ticket count
Case 4 — Bus Full

When seats become:

0

Print:

Bus Full

and stop program automatically.

Important

Program should continue running until:

seats become 0

Use:

loops
conditions
variables
proper flow handling
"""
print("...welcome to bus booking system...")
no_seats=40
user_input1=1
remain_seats=0
while user_input1!=0:
    print(" ")
    user_book=int(input("How many seats do u want : "))
    if no_seats>=user_book:
        print(" ")
        print(f"{user_book} Seats booked succesfully")
        no_seats-=user_book
        remain_seats=no_seats
        print(" ")
        print(f"remaining seats are : {remain_seats}")
    elif no_seats<user_book:
        if no_seats==0:
            print(" ")
            print("..Bus is full..")
        else:
            print(" ")
            print("sorryy..")
            print(f"we have only {remain_seats} seats..")
    else:
        print(" ")
        print("Invalid.. pease enter correct number..")
    print(" ")

    user_input1=int(input("Do u want to book again - yes(any key) no(0) : "))
    if user_input1==0:
        print(" ")
        break
    elif user_input1<0:
        print(" ")
        while True:
            print("invalid input. please enter correct option..")
            user_input1=input("Do u want to book again - yes(any key) no(0) : ")
            print(" ")
    else:
        pass
print(" ")
print("..Thank you for choosing us..")
    


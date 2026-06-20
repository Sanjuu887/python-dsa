"""
3. Grocery Billing System

Items:

Rice = 60/kg
Sugar = 45/kg
Oil = 120/liter

Program should:

ask what item user wants
ask quantity
calculate bill
allow multiple purchases
final bill should print at end
negative balance , then stop that item means 0 grams
enters only available items
calculate bill at last when user dont buy anything

Invalid item:

Item not available
"""
print("....Jaynya's Grocery billing system....")
print(" ")
Rice_quantity=6000
sugar_quantity=4500
oil_quantity=120000

Rice_price=13
sugar_price=25
oil_price=35

bill=0
final_bill=0

user_input1=1

while user_input1!=0:
    print("Items are : Rice(1) , Sugar(2) , Oil(3) onlyy")
    user_input=int(input("Enter the Item number u want : "))
    if user_input!=1 and user_input!=2 and user_input!=3:
        print("Invalid Item..pls select correct item ")
        print(" ")

    else:
        quantity=int(input("Enter how much quantity (in grms) : "))
        if user_input==1 and quantity>=100:
            if Rice_quantity<=0:
                print(f"We have only {Rice_quantity} grms")
                print("sorry , we dont have that much Quantity")
            else:
                if quantity<=Rice_quantity:
                    print(" ")
                    print(f"selected Item number : {user_input} , Item name : Rice")
                    bill=(quantity/100)*Rice_price
                    print("cost: ",bill)
                    print(f"Rice:{quantity}grms packed successfully..")
                    Rice_quantity-=quantity
                else:
                    print("sorry , we dont have that much Quantity")
                    print(f"We have only {Rice_quantity}grms")
        else:
            print("minimum quantity is 100 grams..")
        if user_input==2 and quantity>=100:
            if sugar_quantity<=0:
                print(f"We have only {sugar_quantity} grms")
                print("sorry , we dont have that much Quantity")
            else:
                if quantity<=sugar_quantity:
                    print(f"selected Item number : {user_input} , Item name : Sugar")
                    bill=(quantity/100)*sugar_price
                    print("cost: ",bill)
                    print(f"Sugar: {quantity} grms packed successfully..")
                    sugar_quantity-=quantity
                else:
                    print("sorry , we dont have that much Quantity")
                    print(f"We have only {sugar_quantity}grms")

        if user_input==3 and quantity>=100:
            if oil_quantity<=0:
                print(f"We have only {oil_quantity} grms")
                print("sorry , we dont have that much Quantity")
            else:
                if quantity<=oil_quantity:
                    print(" ")
                    print(f"selected Item number : {user_input} , Item name : Oil")
                    bill=(quantity/100)*oil_price
                    print("cost: ",bill)
                    print(f"Oil: {quantity} grms packed successfully..")
                    sugar_quantity-=quantity
                else:
                    print("sorry , we dont have that much Quantity")
                    print(f"We have only {oil_quantity} grms")

        print(" ")
        final_bill+=bill
    user_input1=int(input("do u want to purchase any item : yes(1) no(any key) : "))
    if user_input1!=1:
        break
    print(" ")
if final_bill==0:
    print(" ")
    print(" Thank u for choosing us..")    
else:
    print(" ")
    print("Total bill: ",final_bill)
    print(" ")
    print("Thank u for choosing us..")  












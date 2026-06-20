"""
Problem 3 — E-Commerce Inventory Manager
Scenario

You own an online store.

Current stock:

Laptop      → 10
Mobile      → 15
Headphones  → 20
Requirements

The program should repeatedly show:

1. View Stock
2. Purchase Product
3. Exit
Option 1 — View Stock

Print all products with available quantity.

Example:

Laptop      : 10
Mobile      : 15
Headphones  : 20
Option 2 — Purchase Product

Ask:

Enter Product Name:

Then ask:

Enter Quantity:
Rules
Rule 1

If product does not exist:

Product Not Found
Rule 2

If quantity entered is:

0 or negative

Print:

Invalid Quantity
Rule 3

If requested quantity is greater than available stock:

Example:

Available Stock: 5
Requested: 10

Print:

Insufficient Stock
Rule 4

If purchase is successful:

Reduce stock.

Print:

Purchase Successful

and show updated stock.

Option 3 — Exit

Print:

Thank You For Shopping

Stop program.

Example Test Case
Choose: 2

Product: Laptop
Quantity: 3

Output:

Purchase Successful

Laptop : 7
Mobile : 15
Headphones : 20
Example Test Case
Choose: 2

Product: Mobile
Quantity: 50

Output:

Insufficient Stock
Example Test Case
Choose: 2

Product: Camera

Output:

Product Not Found
Topics Covered

✅ Dictionaries
✅ Functions (recommended)
✅ Loops
✅ Conditions
✅ Input Validation
✅ State Management
✅ Inventory Tracking

"""

print("Jaynya's Electronic Inventory")
print(" ")

items={
    "laptop":10,
    "mobile":15,
    "headphones":20
}

def get_view_stock(items):
    for name,quantity in items.items():
        print(name," : ",quantity)

def get_purchase_product():
    while True:
        print(" ")
        product_name=input("Enter Product Name : ")
        quantity=int(input("Enter Quantity : "))

        if product_name not in items:
            print(" ")
            print("Product not found")
            break
        
        elif quantity<=0:
            print(" ")
            print("Invalid quantity")
            break
        
        elif items[product_name]<quantity:
            print(" ")
            print("Insufficient Stock ")
            break
        else:
            items[product_name]-=quantity
            print(" ")
            print("Purchase Successful")
            print(" ")

            print("..Updated stock..")
            for name,quantity in items.items():
                print(name," : ",quantity)
            break
                   
while True:
    print("\n1. View Stock\n2.Purchase Product\n3.Exit")
    print(" ")
    choice=int(input("Enter your option : "))
    if choice==1:
        print(" ")
        print(" View Stock")
        get_view_stock(items)

    elif choice==2:
        product=get_purchase_product()
    
    elif choice==3:
        print("Thank you for Shopping")
        break
    else:
        print("Invalid option")
    
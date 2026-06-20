products={
    "rice": 60,
    "sugar":45,
    "oil":120,
    "milk":30
}

cart={}
total_bill=0

print("..Welcome to jaynya's shopping cart..\n")

while True:

    print("\n1. view products\n2. Add products to cart\n3. view cart\n4. checkout\n5. Exit\n")
    option=input("Enter your option here : ")

    if option=="1":
        print("\n... 1. view products ..\n")
        for product, price in products.items():
            print(product,":",price)

    elif option=="2":
        print("\n2. Add to cart products.\n")
        product_name=input("Enter product name : ").lower()
        if product_name not in products:
            print("..product not found..")
            continue
        quantity=int(input("Enter Quantity you want : "))
        if quantity<=0 :
            print("Invalid quantity")
            continue
        if product_name in cart:
            cart[product_name]+=quantity
        else:
            cart[product_name]=quantity
        print("Product added successfully")
    
    elif option=="3":
        print("\n3. View cart.\n")
        if cart is None:
            print("cart is Empty\n")
        else:
            for product , quantity in cart.items():
                cost=products[product]*quantity
                print("\nproduct name : ",product,"\nquantity : ",quantity,"\ncost : ",cost)
    
    elif option=="4":
        print("\n4. Check out\n")
        if cart is None:
            print("cart is Empty\n")
        else:
            for product , quantity in cart.items():
                cost=products[product]*quantity
                print("\nproduct name : ",product,"\nquantity : ",quantity,"\ncost : ",cost)
                total_bill+=cost

            print("\nTotal bill is : ",total_bill)
    elif option=="5":
        print("\nThank you for shopping..")
        break
    else:
        print("\nInvalid option")
    
        
        




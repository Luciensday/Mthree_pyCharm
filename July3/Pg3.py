'''
Program that replicates resaurant model
1 pizza: 10
2 Burger: 5
3 Wraps: 7
4 Exit
We need to ask customer the choice and quantity
the moment choice is 4 we need bill and come out the loops
'''





qty=0
bill = 0

while True:
    print("Please select the menu: \n 1.Pizza: 10 \n 2 Burger: 5 \n 3 Wraps: 7 \n 4 Exit ")
    ch = int(input("Enter the choice =  "))

    if ch >= 1 and ch<=3:
        qty = int(input("Enter the quantity = "))

    if ch == 1:
        price = qty*10
        bill = bill + price
    elif ch ==2:
        price = qty* 5
        bill = bill + price
    elif ch ==3:
        price = qty* 7
        bill = bill + price
    elif ch == 4:
        print("Bill = ", bill)
        break
    else:
        print("Invalid choice")


"""
Other solution ****

def restaurant_order ():
    menu = {1: ("Pizza",10), 2: ("Burger", 5), 3: ("Wraps", 7)}
    bill = 0 
    while True:
        print ("Menu:")
        for key, value in menu.items):
            print(f"{key}. {value[0]}: ${value[1]}")
        print("4. Exit")
    
        choice = int(input("Enter the number of your choice: "))
    
        if choice == 4:
            break
        if choice in menu:
            quantity = int(input (f"Enter the quantity of {menu[choice][0]}: "))
            bill += menu[choice][1] * quantity 
        else:
            print("Invalid choice. Please try again.")
            
    print(f"Your total bill is: £{bill}")
    
"""


#display menu
#take order
#total bill
#add items 
#delete items
menu_items = {
    1:('Tea', 10),
    2:('Milk', 10),
    3:('Coffee',20),
    4:('Boost',15)
}

cart = []

def menu():
    for key,value in menu_items.items():
        print(f'{key}.{value[0]} - {value[1]}rs')




def yourOrder():
    menu()
    try:
        order = input("Enter item number to add to cart: ")
        if order in menu_items:
            cart.append(menu_items[order])
            print(f'{menu_items[order[0]]} added to cart')
        else:
            print("Invalid item number")
    except ValueError:
        print("Please enter a valid number")

def cancleOrder():
    print("This is cancle order function")

def showBill():
    print("This is show bill funciton")
while True:
    print("----- Welcome to Tea Time Cafe -----")
    print("1.Menu")
    print("2.Cancle order")
    print("3.Show Bill")
    print("4.Exit")
    # break
    choice = input("Enter you choice: ")
    
    if choice == "1":
        yourOrder()
    elif choice == "2":
        cancleOrder()
    elif choice == "3":
        showBill()
    elif choice == "4":
        print("Thank you Visit again!")
        break 
    else:
        print("invalid Choice!")

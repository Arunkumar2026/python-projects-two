#display menu
#take order
#total bill
#add items 
#delete items

def menu():
    print("1.Tea - 10rs")
    print("2.Milk - 10rs")
    print("3.Coffee - 20rs")
    print("4.Boost - 15rs")



def yourOrder():
    print("This is place order function")

def cancleOrder():
    print("This is cancle order function")

def showBill():
    print("This is show bill funciton")
while True:
    print("----- Welcome to Tea Time Cafe -----")
    print("1.Menu")
    print("2.Your order")
    print("3.Cancle order")
    print("4.Show Bill")
    print("5.Exit")
    # break
    choice = input("Enter you choice: ")
    if choice == "1":
        menu()
        while True:
            choice = input("your order: ")
            menu_2 = input("Do you want still anything (y/n): ")
            if menu_2 == 'y':
                menu()
            else:
                break

    elif choice == "2":
        yourOrder()
    elif choice == "3":
        cancleOrder()
    elif choice == "4":
        showBill()
    elif choice == "5":
        print("Good Bye")
        break 
    else:
        print("invalid Choice!")
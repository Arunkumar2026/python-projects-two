#This is a list program
'''In this program there will be four topics that are list, conditions, functions and control statements'''
#in list how to create a empty list, how to add elements to list, how to access list items, how to delete list items
#list
#control statements
#conditions
#functions

def createList():
    return []


def addString(my_list):
    while True:
        add = input("Add item (y/n): ").lower()
        if add == "y":
            string = input("Enter the value: ")
            my_list.append(string)
            print(my_list)
        elif add == "n":
            return my_list
        else:
            print("Please enter y (yes) or n (no)")


def addInt(my_list):
    while True:
        try:
            num = int(input("Enter the value: "))
            my_list.append(num)
            print(my_list)
        except ValueError:
            print("Please enter valid number")
        







def addToList(my_list):
        print("What data type do you want to add?")
        print("1. String")
        print("2. Integer")
        print("3. Boolean")
        data_choice = input("Enter you choice: ")
        if data_choice == "1":
            string = addString(my_list)
            return string 
            # print(f'your list:- {str}')
        elif choice == "2":
            integer = addInt(my_list)
            return  integer
            # print(f'your list:- {integer}')



print("-----Welcome to list practice-----")
while True:
    print("\n1. Create list")
    print("2. Add items")
    choice = input("Enter your choice: ")
    if choice == "1":
        my_list = createList()
        print(f'Empty list:- {my_list}\n')
        print("----------------------------------------\n")
        # break
    elif choice == "2":
        addToList(my_list)
        break



''''
def create_list():
    return []


def add_string(my_list):
    value = input("Enter string value: ")
    my_list.append(value)
    print("Updated List:", my_list)


def add_int(my_list):
    try:
        value = int(input("Enter integer value: "))
        my_list.append(value)
        print("Updated List:", my_list)
    except ValueError:
        print("Invalid integer!")


def add_bool(my_list):
    value = input("Enter boolean (true/false): ").lower()
    if value == "true":
        my_list.append(True)
    elif value == "false":
        my_list.append(False)
    else:
        print("Invalid boolean!")
        return
    print("Updated List:", my_list)


def delete_item(my_list):
    if not my_list:
        print("List is empty!")
        return

    print("Current List:", my_list)
    value = input("Enter value to delete: ")

    if value.isdigit():
        value = int(value)
    elif value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False

    if value in my_list:
        my_list.remove(value)
        print("Item removed!")
    else:
        print("Item not found!")

    print("Updated List:", my_list)


def show_list(my_list):
    print("Current List:", my_list)


# ---------------- MAIN PROGRAM ----------------

print("----- Welcome to List Practice -----")

my_list = create_list()

while True:
    print("\n1. Add Item")
    print("2. Delete Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nWhat type do you want to add?")
        print("1. String")
        print("2. Integer")
        print("3. Boolean")

        type_choice = input("Enter choice: ")

        if type_choice == "1":
            add_string(my_list)
        elif type_choice == "2":
            add_int(my_list)
        elif type_choice == "3":
            add_bool(my_list)
        else:
            print("Invalid type choice!")

    elif choice == "2":
        delete_item(my_list)

    elif choice == "3":
        show_list(my_list)

    elif choice == "4":
        print("Goodbye Arun 👋 Keep Practicing!")
        break

    else:
        print("Invalid choice!")

'''


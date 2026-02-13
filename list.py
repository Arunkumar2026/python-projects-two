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



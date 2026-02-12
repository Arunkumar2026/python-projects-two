#This is a list program
'''In this program there will be four topics that are list, conditions, functions and control statements'''
#in list how to create a empty list, how to add elements to list, how to access list items, how to delete list items
#list
#control statements
#conditions
#functions

def createList():
    return []

def addToList():
    print("What data type do you want to add?")
    print("1. String")
    print("2. Integer")
    print("3. Boolean")
    data_choice = input("Enter you choice: ")
    if data_choice == "1":
        pass


print("-----Welcome to list practice-----")
while True:
    print("1. Create list\n")
    print("2. Add items to list\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        result = createList()
        print(f'Empty list:- {result}\n')
        print("----------------------------------------\n")
        # break
    elif choice == "2":
        addToList()
        break



# this program will print the digits in words
'''
def printNums(digit):
    if digit == "1":
        print("one", end=" ")
    elif digit == "2":
        print("two", end=" ")
    elif digit == "3":
        print("three", end=" ")
    elif digit == "4":
        print("four", end=" ")
    elif digit == "5":
        print("five", end=" ")
    elif digit == "6":
        print("six", end=" ")
    elif digit == "7":
        print("seven", end=" ")
    elif digit == "8":
        print("eight", end=" ")
    elif digit == "9":
        print("nine", end=" ")
    elif digit == "0":
        print("zero", end=" ")
    print()

def printWord(n):
    i = 0
    length = len(n)
    while i < length:
        printNums(n[i])
        i += 1



while True:
    num = input("Enter you Number: ")
    printWord(num)
'''

def divisible(divident, divisor):
    if divident % divisor == 0:
        return True
    return False 
    

while True:
    divident = int(input("Enter the divident number: "))
    divisor = int(input("Enter the divisor number: "))

    print(divisible(divident, divisor))
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
'''
def divisible(divident, divisor):
    if divident % divisor == 0:
        return True
    return False 
    

while True:
    divident = int(input("Enter the divident number: "))
    divisor = int(input("Enter the divisor number: "))

    print(divisible(divident, divisor))
'''

num = 2
print(type(num))
string = str(num)
print(type(string))

floating = float(num)
print(type(floating))
boolean = bool(num)
print(type(boolean))
print(num)
a,b = 10,20
print(a)

c = d = e = 100
print(c,d,e)

s = 'arun'
print(s)
s1 = "kum"      \
"ar"
print(s1)
s2 = '''aru
n
kumar'''
print(s2)


emptylist = []
print(type(emptylist))
emptytuple = ()
print(type(emptytuple))
emptydict = {}
print(type(emptydict))
emptyset = set()
print(type(emptyset))



list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
list1.pop()
print(list1)
list1.append(9)
print(list1)
listslicing = list1[:]
print(listslicing)
listslicing2 = list1[1:]
print(listslicing2)
listslicing3 = list1[:2]
print(listslicing3)
n = "3"
listslicing4 = list1[::int(n)]
print(listslicing4)

changelilst = list1[1] = 56 
print(changelilst)
print(list1)
list1[3:7] = [0,0,0,0]
print(list1)
list1[2] = 20
print(list1)
list1.insert(2,10)
print(list1)

newlist = [1,'arun', True]
print(newlist)
import random

print("----- Welcome to number guessing game -----\n")

msg = '''In this game you have to give two positive number, first number should be less than second number
and when the game starts you have to guess the number between the given numbes, you will have "7" chances 
to guess the correct number.'''
print(msg)
print("ALL THE BEST!")

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

random_num = random.randint(first_num, second_num)
chances = 7
guess_conter = 0
# print(random_num)

while guess_conter < chances:
    guess_conter += 1
    guess = int(input("Enter you guess number: "))

    if guess == random_num:
        print("Congratulations, You guessed the correct number!")
        break
    elif guess_conter >= chances:
        print(f'Sorry you guessed the wrong number! the correct number is {random_num}')
    elif guess > random_num:
        print("Too High")
    elif guess < random_num:
        print("Too Low")
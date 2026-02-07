import random
def game():
    words = ['rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    #print(words)
    msg = "in the given words you have to guess the correct word in 7 chances"
    print(msg)

    chances = 7
    while chances > 0:
        print(words)
        guess = input("Guess the word: ").lower()
        chances -= 1
        if guess == word:
            print("Congrulation, You guessed correct!")
            return
        elif chances > 0 and guess != word:
            print(f'Wrong guess, Try again you have {chances} chances')
            if guess in words:
                words.remove(guess.lower())
    
    print(f'You Loos, your chances are finished.')
    print(f'correct word is {word}')

print("----- Welcome you word guessing game -----")
msg = '''In this game you will be given 12 random words your task is you find the correct 
word in the game. You will have 7 chances you guess the correct word. ALL THE BEST'''
print(msg)
ready = input("Are you ready (y/n): ")
if ready == "y":
    while True:
        game()
        choice = input("want you play again (y/n): ")
        if choice != 'y':
            print("----- Thanks you! -----")
            break
else:
    print("Good bye!")
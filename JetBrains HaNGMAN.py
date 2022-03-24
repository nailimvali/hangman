import random

while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
    if menu == 'play':
        chosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
        print('H A N G M A N')
        hidden = list('-' * len(chosen))
        inserted_letters = []
        j = 0
        while j < 8:
            print()
            print(''.join(hidden))
            guess = input('Input a letter: ')
            if len(guess) == 1 and 97 <= ord(guess) <= 122:
                inserted_letters.append(guess)
            if guess in chosen and guess not in hidden:
                for i in range(len(chosen)):
                    if chosen[i] == guess:
                        hidden[i] = guess
            elif inserted_letters.count(guess) >= 2 and len(guess) == 1:
                print("You already typed this letter")
            elif len(guess) != 1:
                print("You should input a single letter")
            elif ord(guess) < 97 or ord(guess) > 122:
                print("It is not an ASCII lowercase letter")
            else:
                print('No such letter in the word')
                j += 1
            if "-" not in hidden:
                print(''.join(hidden))
                print("You guessed the word!\nYou survived!")
                break
        if j == 8:
            print("You are hanged!")
            break
    elif menu == "exit":
        break
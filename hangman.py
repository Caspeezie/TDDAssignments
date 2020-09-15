import random
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
===========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    0   |
    |   |
        |
        |
===========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
===========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
===========''', '''

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
===========''', '''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
===========''']
colours = 'red blue green brown black purple white pink orange silver indigo grey lilac yellow gold'.split()

def getRandomColour(colourList):
    colourIndex = random.randint(0, len(colourList) -1)
    return colourList[colourIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
            else:
                return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswitch('y')


print('H A N G M A N')
missedletters = ' '
correctLetters = ' '
secretWord = getRandomWord(colours)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The esecret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) = len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + 'missed guesses and ' + str(len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

            # Ask the player if they want to play again (but if only the game is done)
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(colours)
                else:
                    break

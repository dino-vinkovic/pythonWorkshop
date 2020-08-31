import random


# Select and return random word from provided list of words
def getRandomWord(wordsList):
    randomWordIndex = random.randrange(0, len(words))

    return wordsList[randomWordIndex]


# Check the letter and return the word with guessed letters shown
def checkLetter(secretWord, alreadyGuessed):

    currentGuess = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in alreadyGuessed:
            currentGuess = currentGuess[:i] + secretWord[i] + currentGuess[i + 1:]

    return currentGuess


# Check the input and return the letter or secret word if guessed. Otherwise, tell user to input a letter / solution
def getGuess(alreadyGuessed, secretWord):
    while True:
        guessLetter = input('\nGuess a letter or the word: ').lower()

        if guessLetter == secretWord:
            return secretWord
        elif len(guessLetter) != 1:
            print('\nPlease enter a single letter or the solution.')
        elif guessLetter in alreadyGuessed:
            print('\nYou have already guessed that letter. Guess again.')
        else:
            return guessLetter


words = ['animal', 'abacus', 'clown', 'music', 'instrument', 'language', 'apartment', 'planet', 'number', 'computer']

print('''* * * H A N G M A N * * *
   +---+
   |   |
       |
       |
       |
       |
=========\n''')

# Get random word from the list of words and print it replaced by underscores
randomPlayWord = getRandomWord(words)
print('Guess the word: ', '_' * len(randomPlayWord))

movesCount = 10
guessedSoFar = ''

while movesCount > 0:

    # Get user input a letter or solution and check what he typed in
    guess = getGuess(guessedSoFar, randomPlayWord)

    if guess in randomPlayWord:
        print('\nYou guessed the letter: ', guess)
        guessedSoFar += guess
        guessedSoFar = checkLetter(randomPlayWord, guessedSoFar)
        print(guessedSoFar)

        if guess == randomPlayWord or guessedSoFar == randomPlayWord:
            print('Congratulations! You guessed it!')
            break
    elif movesCount > 1:
        print('\nGuess again. You have ' + str(movesCount - 1) + ' guesses left.')
        movesCount -= 1
    else:
        print('Game over.')
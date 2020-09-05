import random


# Select and return random word from provided list of words
def get_random_word(words_list):
    random_word_index = random.randrange(0, len(words))

    return words_list[random_word_index]


# Check the letter and return the word with guessed letters shown
def check_letter(secret_word, already_guessed):
    current_guess = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in already_guessed:
            current_guess = current_guess[:i] + secret_word[i] + current_guess[i + 1:]

    return current_guess


# Check the input and return the letter or secret word if guessed. Otherwise, tell user to input a letter / solution
def get_guess(secret_word, already_guessed):
    while True:
        guess_letter = input('\nGuess a letter or the word: ').lower()

        if guess_letter == secret_word:
            return secret_word
        elif len(guess_letter) != 1:
            print('\nPlease enter a single letter or the solution.')
        elif guess_letter in already_guessed:
            print('\nYou have already guessed that letter. Guess again.')
        else:
            return guess_letter


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
random_play_word = get_random_word(words)
print('Guess the word: ', '_' * len(random_play_word))

count_moves = 10
guessed_so_far = ''

while count_moves > 0:

    # Get user input a letter or solution and check what they typed in
    guess = get_guess(guessed_so_far, random_play_word)

    # Check whether the guessed letter is in the secret word
    if guess in random_play_word:
        print('\nYou guessed the letter: ', guess)
        guessed_so_far += guess
        guessed_so_far = check_letter(random_play_word, guessed_so_far)
        print(guessed_so_far)

        # Check if solution was offered or if all the letters were guessed and form the complete word
        if guess == random_play_word or guessed_so_far == random_play_word:
            print('Congratulations! You guessed it!')
            break
    elif count_moves > 1:
        print('\nGuess again. You have ' + str(count_moves - 1) + ' guesses left.')
        count_moves -= 1
    else:
        print('Game over.')

import random


# Prompt user for name. Check the input consists of letters
def input_name(name):
    while not name.isalpha():
        print("Please use letters only. Names like 'X Æ A-12' are a bit weird.")
        name = input("Type in the player's name again: ")

    return name


# Randomly choose which player goes first
def choose_first_player():
    goes_first = random.choice([player_one, player_two])

    if goes_first == player_one:
        print(player_one + " is X. \n" + player_two + " is O.")
    else:
        print(player_two + " is X. \n" + player_one + " is O.")

    print(goes_first + " goes first.")

    return goes_first


# Draw the board
def draw_board():
    print('\n %c  |  %c  |  %c ' % (board[1], board[2], board[3]))
    print('___ | ___ | ___')
    print(' %c  |  %c  |  %c ' % (board[4], board[5], board[6]))
    print('___ | ___ | ___')
    print(' %c  |  %c  |  %c ' % (board[7], board[8], board[9]))


# Prompt the user to select a field and check the input is valid
def choose_field(player):
    chosen_field = 0

    while chosen_field not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        chosen_field = input(player + ', select a field [1 - 9]: ')

        try:
            chosen_field = int(chosen_field)

            if not type(chosen_field) is int:
                raise ValueError
        except ValueError:
            pass

    return chosen_field


# Check for horizontal / vertical / diagonal win or draw. Continue otherwise
def check_game_status():
    if ((board[1] == board[2] == board[3] != ' ') or
        (board[4] == board[5] == board[6] != ' ') or
        (board[7] == board[8] == board[9] != ' ') or
        (board[1] == board[4] == board[7] != ' ') or
        (board[2] == board[5] == board[8] != ' ') or
        (board[3] == board[6] == board[9] != ' ') or
        (board[1] == board[5] == board[9] != ' ') or
            (board[3] == board[5] == board[7] != ' ')):
        status = 'Win'
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and
            board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        status = 'Draw'
    else:
        status = 'Continue'

    return status


# Check whether the field has already been filled in
def check_field_validity(field):
    if board[field] == ' ':
        return True
    else:
        print('The field has already been filled in. Please select another one.')
        return False


print("""* * * Tic Tac Toe * * * 
        |     |
    [1] | [2] | [3]
    ___ | ___ | ___
        |     |
    [4] | [5] | [6]
    ___ | ___ | ___
        |     |
    [7] | [8] | [9]
        |     |
""")


# Prompt user for two names
player_one = input_name(input("Player One, what's your name: "))
player_two = input_name(input("Player Two, what's your name: "))

# Random choice who goes first
current_player = choose_first_player()

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
mark = 'X'
game_status = 'Continue'

# Draw blank board the first time
draw_board()

while game_status == 'Continue':

    # Prompt user to choose a field
    selected_field = choose_field(current_player)

    # Check whether the field has already been filled in
    # If available, type in the current player's mark starting with 'X'
    if check_field_validity(selected_field):
        board[selected_field] = mark
        # Check the status of the game and draw the current board
        game_status = check_game_status()
        draw_board()

        # Check the game status
        if game_status == 'Win':
            print(current_player + ' is the winner!')
            break
        elif game_status == 'Draw':
            print('Draw.')
            break

        # Change marks
        if mark == 'X':
            mark = 'O'
        else:
            mark = 'X'

        # Change turns
        if current_player == player_one:
            current_player = player_two
        else:
            current_player = player_one

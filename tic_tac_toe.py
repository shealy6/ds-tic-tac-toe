# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Let players add names, choose a symbol

# Function for displaying the board in 3x3 grid form
def show_board(x):
    print(x[:3])
    print(x[3:6])
    print(x[6:])

# Trying a better way to show the board
def show_board_2(y):
    for i in range(0, 9, 3):    # gets the startting index of each row
        row = y[i:i + 3]        # gets each row
        print(" | ".join(str(cell) for cell in row)) # joins each cell as a string with a divider
        if i < 6:
            print("--+---+--") # Create a break after both of the first two rows

    

#Defining a function for move validation
def check_move(move_1: int, board_1):               # move must be int, and is checked against the current board state
    if move_1 not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:   # must be in the range [1,9]
        print("Choose a valid move")
        return False
    elif board_1[move_1-1] in ("X", "O"):           # must be in a free space 
        print("Choose an open space")
        return False
    else:
        return True


# Asks for input and checks move is valid, then returns the valid move
def get_move(board):
    while True:
        try:
            move = int(input("Your move (1-9): "))  # makes sure the input is an integer
        except ValueError:
            print("Please enter a number.")         # Deals with errors for non-integer values
            continue
        if check_move(move, board):                 # Checks moves validity, if false, prints why and returns to start of the loop
            return move

# Checking for a win after a player moves
def check_winner(board, player):
    rows = [board[0:3], board[3:6], board[6:9]]     # defining three in a row
    cols = [board[0::3], board[1::3], board[2::3]]  # defining three in a column
    diags = [board[0::4], board[2:7:2]]             # defining three in a diagonal
    win = [player] * 3                              # making three Xs or Os depending on the turn
    return win in rows + cols + diags               # Returns True if it finds three in a row


# Defining the function for playing the game
def play_game():
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = list(range(1, 10))  # Creates the "board" list
    show_board_2(board)

    for move_number in range(1, 10):
        player = "X" if move_number % 2 == 1 else "O"   # Checks whose turn it is and defines player as X or O
        print(f"{player}'s turn. Move {move_number}. Choose a number to make your move!")

        move = get_move(board)
        board[move - 1] = player
        show_board_2(board)

        if check_winner(board, player):
            print(f"Nice move! {player} wins!")
            return

    print("It's a draw!")

# Defining a function to play again
def play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")

# Tic-tac-toe game
if __name__ == "__main__":
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing!")
            break
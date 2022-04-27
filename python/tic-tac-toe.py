#tic-tac-tow game with python by Juan Carlos Munive

#grid for the board
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

#variable to verify if the game is still going
game_going = True

#Variable to store who win or if it was a tie
winner = None

#Variable to know the current player
player = 'X'



def show_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def main():
    #first thing to do create the board to be able to play.
    show_board()

    #loop to keep the game running until is over.
    while game_going:

        manage_turns(player)

        check_game_over()

        change_player()

        #end of the game
        if winner == 'X' or winner == 'O':
            print(f'{winner} won.')
        elif winner == None:
            print('Tie.')
    
    
#fuctions to manage turns
def manage_turns(player):
    square = int(input(f'{player}\'s turn to choose a square (1-9):'))
    square = square - 1
    board[square] = 'X'
    show_board()
    pass

#verify if the game is over either win or tie
def check_game_over():
    check_win()
    check_tie()

#functions to verify who won and to check the rows, columns and diagonals
def check_winner():
    #call global variable
    global winner

    row_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None

def check_rows():
    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]

def check_columns():
    pass
def check_diagonals():
    pass

#verify if one player has won
def check_win():
    pass

#verify if there is a tie
def check_tie():
    pass

#Change between players
def change_player():
    pass



main()

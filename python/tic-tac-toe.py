#tic-tac-tow game with python by Juan Carlos Munive
#importing os to be able to use system to clear the terminal
import os

#grid for the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


#variable to verify if the game is still going
game_going = True

#Variable to store who win or if it was a tie
winner = None

#Variable to know the current player
player = 'X'



def show_board():
    print("\n")
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '     1 | 2 | 3')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '     4 | 5 | 6')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '     7 | 8 | 9')
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
        print('It is a tie.')
    
    
#fuctions to manage turns
def manage_turns(player):
    square = input(f'{player}\'s turn to choose a square (1-9): ')
    #while loop to make sure that a player is not playing on an already played square.
    valid = False
    while not valid:
        #validate if the input is correct
        while square not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            square = input(f'Enter a valid option, choose a square (1-9): ')
        
        square = int(square) - 1

        #check if the square is available
        if board[square] == "-":
             valid = True
        else:
            print("That square is not available to play. Go again.")

    #puts the play in the board        
    board[square] = player
    #command to clear the screen
    os.system('cls')
    show_board()
    pass

#verify if the game is over either win or tie
def check_game_over():
    check_winner()
    check_tie()

#functions to verify who won and to check the rows, columns and diagonals
def check_winner():
    #call global variable
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
     # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None

#verify if there is a tie
def check_tie():
    global game_going
    if '-'  not in board:
        game_going = False

#Change between players
def change_player():
    global player
    #changes between x and o to determine the player every turn.
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'



main()

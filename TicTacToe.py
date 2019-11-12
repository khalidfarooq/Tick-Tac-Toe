board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going= True

winner = None
6
current_player = "X"

def display_board():
    # displaying the board to user

    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")

def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)
        chk_if_game_over()
        flip_player()

    if winner == "X" or winner == 'O':
        print(winner + " won")
    elif winner == None:
        print("Tie")


def handle_turn(player):

    print(player +"'s turn.")

    valid = False
    while not valid:
        position =0

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position]=player

    display_board()

def chk_if_game_over():
    chk_winner()
    chk_tie()


def chk_winner():
    global winner

    row_winner =chk_rows()
    coloumn_winner =chk_coloumn()
    diagonal_winner=chk_diagonal()

    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def chk_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going= False

    if row_1:
        return board[0]
    elif row_2:
        return  board[3]
    elif row_3:
        return  board[6]
    else:
        return None


def chk_coloumn():
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def chk_diagonal():
    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2 :
        game_still_going = False

    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    else:
        return None

def chk_tie():
    global game_still_going

    #if board is full so its a tie
    if "-" not in board:
        game_still_going=False
        return True
    #else there is no tie
    else:
        return  False
def flip_player():
    global current_player

    if current_player=="X":
        current_player= "O"
    elif current_player == "O":
        current_player= "X"


play_game()








# Tic-Tac-Toe
from guizero import App, Box, PushButton, Text


def clear_board():
    new_board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]
    
    for x in range(0, 3, 1):
        for y in range(0, 3, 1):
            button = PushButton(master = board, text = "", grid = [x, y], width = 3, command = choose_square, args = [x, y])
            # button.bg = "orange"
            new_board[x][y] = button
    
    return new_board

def choose_square(x, y):
    board_square[x][y].text = turn
    board_square[x][y].disable() # Disabling the button click after clicking once.
    toggle_player()
    check_win()


def toggle_player():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    message.value = "It is your turn, " + turn

def check_win():
    winner = None

    # Vertical lines --> |
    if (board_square[0][0].text == board_square[0][1].text == board_square[0][2].text) and (board_square[0][2].text in ["X", "O"]): 
        winner = board_square[0][0]

    # This condition check the text "X" and "O" correctly.
    elif (board_square[1][0].text == board_square[1][1].text == board_square[1][2].text) and (board_square[1][2].text in ["X", "O"]):
        winner = board_square[1][0]

    elif (board_square[2][0].text == board_square[2][1].text == board_square[2][2].text) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[2][0]
    
    # Horizontal lines --> -- # This condition and board_square[2][0].text in ["X", "O"] is indeed needed.
    elif (board_square[0][0].text == board_square[1][0].text == board_square[2][0].text) and board_square[2][0].text in ["X", "O"]:
        winner = board_square[0][0]

    elif (board_square[0][1].text == board_square[1][1].text == board_square[2][1].text) and board_square[2][1].text in ["X", "O"]:
        winner = board_square[0][1]

    elif (board_square[0][2].text == board_square[1][2].text == board_square[2][2].text) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[0][2]

    # Diagonal lines
    elif (board_square[0][0].text == board_square[1][1].text == board_square[2][2].text) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[0][0]
 
    elif (board_square[2][0].text == board_square[1][1].text == board_square[0][2].text) and board_square[0][2].text in ["X", "O"]:
        winner = board_square[2][0]

    if winner is not None:
        message.value = winner.text + " Wins!"

    elif moves_taken() == 9:
        message.value = "It is a Draw! Play again"


def moves_taken():
    moves = 0
    for row in board_square:
        for col in row:
            if (col.text == "X") or (col.text == "O"):
                moves += 1 
    return moves


def reset():
    global board_square, message
    board_square = clear_board()


turn = "X"

app = App(title = "Tic Tac Toe")

big_title = Text(master = app, text = "👉Tic Tac Toe👈")
big_title.size = 16

board = Box(master = app, layout = "grid")
board.bg = "Orange"
board_square = clear_board()

message = Text(master = app, text = "It is your turn, " + turn)
message.text_color = "red"

reset_button = PushButton(master = app, command = reset, text = "Reset")
reset_button.bg = "green"


# message2 = Text(master = app, text = "I am testing the box grid layout")
# board2 = Box(master = app, layout = "grid")
# for i in range(0, 3, 1):
#     for j in range(0, 3, 1):
#         PushButton(master = board2, text = f"{i=}, {j=}", grid = [i, j], width = 3)
app.display()
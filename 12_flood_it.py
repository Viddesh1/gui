########################
# IMPORTS
########################

from guizero import App, Waffle, Text, PushButton, info
from random import choice


########################
# Variables
########################

board_size = 10
colours = ["red", "green", "blue", "yellow", "orange", "purple"]
moves_limit = 25
moves_taken = 0

########################
# Functions
########################

def flood(x, y, target, replacement):
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y + 1 <= board_size - 1: # south
        flood(x, y+1, target, replacement)
    if y - 1 >= 0: # North
        flood(x, y - 1, target, replacement)
    if x+1 <= board_size - 1: # East
        flood(x + 1, y, target, replacement)
    if x - 1 >= 0: # West
        flood(x - 1, y, target, replacement)

# Check whether all the squares are same
def all_squares_are_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False
    
def win_check():
    global moves_taken
    moves_taken += 1
    if moves_taken <= moves_limit:
        if all_squares_are_same():
            win_text.value = "You Win!"
    else:
        win_text.value = "You lost!"

def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, choice(colours))

def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour), 0, colour)


def start_flood(x, y):
    flood_colour = palette.get_pixel(x, y)
    target = board.get_pixel(0, 0)
    flood(0, 0, target, flood_colour)
    win_check()


########################
# APP
########################
app = App(title = "Flood it")
board = Waffle(master = app, height = board_size, width = board_size)
palette = Waffle(master = app, height = 1, width = 6, dotty = True, command = start_flood)
win_text = Text(app)

fill_board()
init_palette()

app.display()
from guizero import App, Text, Waffle
from random import randint


# Constants Variable
GRID_SIZE : int = 10 # Update this according to the number in board_width and board_height
score : int = 0
board_width, board_height = 10, 10


# Random dots to be appear in the waffle widget.
def add_dot():
    x, y = (randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1))
    while board[x, y].dotty == True:
        x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")

    speed = 1000
    if score > 10:
        speed = 500
    elif score > 20:
        speed = 400
    elif score > 30:
        speed = 300
    elif score > 40:
        speed = 200
    elif score > 50:
        speed = 100

    all_red = True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x, y].color != "red":
                all_red = False
    
    if all_red == True:
        score_display.value = "You lost! Score:- " + str(score)
    else:
        board.after(time = speed, function = add_dot)
    

def destroy_dot(x, y):
    global score
    if board[x, y].dotty == True:
        board[x, y].dotty = False
        board.set_pixel(x, y, "white")
        score = score + 1
        score_display.value = "Your Score:- " + str(score)


app = App(title = "Destroy the Dots")
instructions = Text(master = app, text = "Click the dots to destroy them")
# Waffle widget is automatically passing the 2 parameters x and y for function destroy_dot()
board = Waffle(master = app, width = board_width, height = board_height, command = destroy_dot)
board.after(time = 1000, function = add_dot) # Calling the function after every one second
score_display = Text(master = app, text = "Your Score:- " + str(score))
app.display()
# Tic-Tac-Toe
from guizero import App, Box, PushButton

app = App(title = "Tic Tac Toe")

board = Box(master = app, layout = "grid")
for x in range(0, 3, 1):
    for y in range(0, 3, 1):
        button = PushButton(master = app, text = "", grid = [x, y], width = 3)

app.display()
from guizero import App, Text, Waffle
from random import randint


def add_dot():
    x, y = (randint(0, 4), randint(0, 4))

app = App(title = "Destroy the Dots")
instructions = Text(master = app, text = "Click the dots to destroy them")
board = Waffle(master = app, width = 5, height = 5)

app.display()
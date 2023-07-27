# Imports
from guizero import App, Text, PushButton, Picture
from random import choice

# Functions
def choose_name():
    # print("button was pressed")
    first_names = ["Shadow", "Pokemon", "Leo", "Itachi"]
    last_names = ["Spider", "pikachu", "dragon", "not_uchiha"]
    spy_name = choice(first_names) + " " + choice(last_names)
    # print(spy_name)
    name.value = spy_name
    
# App
app = App(title = "TOP SECRET")

# Widgets
title = Text(app, "Push the big red button to find out your spy name")

button = PushButton(app, choose_name, text = "Tell me!")
button.bg = "red"
# button.height = 5
# button.width = 20
button.text_size = 20

name = Text(app, text = "")
name.text_size = 20

red_guy = Picture(app, image = "among_us_red_guy.png")

# Display
app.display()
# The Emoji Match game. Play and have fun
# You would need to download the emojis from https://magpi.cc/guizeroemojis

########################
# IMPORTS
########################

import os
from random import shuffle, randint
from guizero import App, Box, Picture, PushButton, Text


########################
# Variables
########################

# Setting the path to the emoji folder for program to access
emojis_dir = "emojis"
emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir)]
shuffle(emojis)

########################
# Functions
########################

def setup_round():
    for picture in pictures:
        picture.image = emojis.pop()

    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, args = [False])

    matched_emoji = emojis.pop()

    random_picture = randint(0, 8)
    pictures[random_picture].image = matched_emoji

    random_button = randint(0, 8)
    buttons[random_button].image = matched_emoji

    buttons[random_button].update_command(match_emoji, args = [True])


def match_emoji(matched):
    if matched:
        result.value = "Correct"
        score.value = int(score.value) + 1
    else:
        result.value = "Incorrect"
        score.value = int(score.value) - 1

    setup_round()

def reduce_time():
    timer.value = int(timer.value) - 1
    # Check if the game is over or not
    if int(timer.value) < 0:
        result.value = "Game Over! Score :- " + score.value
        # Hide the game
        pictures_box.hide()
        buttons_box.hide()
        timer.hide()
        score.hide()

########################
# APP
########################
app = App(title = "Emoji's Match")

game_box = Box(master = app, align = 'top')

top_box = Box(master = game_box, align = "top", width = "fill")
Text(master = top_box, align = "left", text = "Score ")
score = Text(master = app, text = "0", align = "left")
timer = Text(master = app, text = "30", align = "right")
Text(master = top_box, text = "Time", align = "right")

pictures_box = Box(master = app, layout = "grid")
buttons_box = Box(master = app, layout = "grid")

pictures = []
buttons = []

for x in range(0, 3, 1):
    for y in range(0, 3, 1):
        picture = Picture(master = pictures_box, grid = [x, y])
        pictures.append(picture)

        button = PushButton(master = buttons_box, grid = [x, y])
        buttons.append(button)


result = Text(master = app)

setup_round()

app.repeat(1000, reduce_time)

app.display()
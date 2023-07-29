from guizero import App, Text


def flash_text():
    if title.visible == True:
        title.hide()
    else:
        title.show()

app = App(title = "Learning GUI in wrong way!", bg = "dark green")
title = Text(app, text = "Something this is hard to read. \n But you are reading it. \n Are you still reading it?",
             font = "Comic Sans", size = 10, color="red", bg = "green")

app.repeat(1000, flash_text)

app.display()

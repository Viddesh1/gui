from guizero import App, Combo
from string import ascii_letters

app = App(title = "GUI done wrong part 2")

app.info(title = "Application Started...", text = "Well Done! You started the application")
app.warn(title = "Application Already Started", text = "It is already started")
app.error(title = "APPLICATION STARTED", text = "Started!!!")

a_letter = Combo(app, options = " " + ascii_letters)
b_letter = Combo(app, options = " " + ascii_letters)

for _ in range(0, 27):
    Combo(app, options = " " + ascii_letters, align = "left")

app.display()
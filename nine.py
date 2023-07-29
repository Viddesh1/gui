from guizero import App, Window


app = App(title = "Main Window")

window = Window(master = app, title = "Second Window")
window.show(wait = True)

app.display()
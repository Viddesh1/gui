from guizero import App, TextBox, Drawing


def draw_meme():
    meme.clear()
    meme.image(x = 0, y = 0, image = "my.png")
    meme.text(x = 20, y = 20, text = top_text.value)
    meme.text(x = 20, y = 320, text = buttom_text.value)


app = App(title = "MEME")

top_text = TextBox(app, text = "top text")
buttom_text = TextBox(app, text = "buttom text")

meme = Drawing(app, width = "fill", height = "fill")

app.display()
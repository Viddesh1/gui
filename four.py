from guizero import App, TextBox, Drawing


def draw_meme():
    meme.clear()
    meme.image(x = 0, y = 0, image = "cat.png")
    meme.text(x = 20, y = 20, text = top_text.value, color = "orange", size = 40, font = "courier")
    meme.text(x = 20, y = 320, text = buttom_text.value, color = "red", size = 40, font = "courier")


app = App(title = "MEME")

top_text = TextBox(app, text = "top text", command = draw_meme)
buttom_text = TextBox(app, text = "buttom text", command = draw_meme)

meme = Drawing(app, width = "fill", height = "fill")

draw_meme()
app.display()
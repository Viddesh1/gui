# Create your own MEME's LOL 
from guizero import App, TextBox, Drawing, Combo, Slider


def draw_meme():
    meme.clear()
    meme.image(x = 0, y = 0, image = "cat2.png")
    meme.text(x = 20, y = 20, text = top_text.value, color = color.value, size = size.value, font = font.value)
    meme.text(x = 20, y = 320, text = buttom_text.value, color = "red", size = size.value, font = font.value)



app = App(title = "MEME")

top_text = TextBox(app, text = "Top Text", command = draw_meme)

buttom_text = TextBox(app, text = "Buttom Text", command = draw_meme)

color = Combo(app, 
              options = ["red", "black", "blue", "green", "orange", "purple"],
              command = draw_meme, selected = "blue")

font = Combo(app, options = ["times new roman", "verdana", "courier", "impact"],
             command = draw_meme, selected = "courier")

size = Slider(app, start = 20, end = 50, command = draw_meme)


meme = Drawing(app, width = "fill", height = "fill")

app.display()
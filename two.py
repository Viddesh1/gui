from guizero import App, Text, Picture

app = App(title = "Wanted!")
app.bg = "#FBFBD0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"

beerus_sama_pic = Picture(app, image = "cat.png")

app.display()
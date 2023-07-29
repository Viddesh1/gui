from guizero import App, PushButton


def are_you_sure():
    if app.yesno("title = Confirmation!", text = "Are you sure?"):
        app.info(title = "Thanks!", text = "Thanks, For confirming")
    else:
        app.error(title = "Error Occured...", text = "You have to confirm to our policies")


app = App(title = "Pop up magic")
button = PushButton(master = app, command = are_you_sure)

app.display()
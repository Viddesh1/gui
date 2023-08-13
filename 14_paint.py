########################
# IMPORTS
########################

from guizero import App, Drawing

########################
# VARIABLES
########################

########################
# FUNCTIONS
########################

def draw(event):
    painting.line(
        painting.last_event.x, painting.last_event.y,
        event.x + 1, event.y + 1, 
        color = 'black',
        width = 3
    )

    painting.last_event = event

def start(event):
    painting.last_event = event


########################
# APP
########################

app = App(title = "Your own custom Paint")

painting = Drawing(master = app, width = 'fill', height = 'fill')
painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw

app.display()
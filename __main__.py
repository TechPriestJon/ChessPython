import pyglet
from pyglet.window import mouse
from components.button import Button
from state.state import State

window = pyglet.window.Window(fullscreen=False)
windowHeight = window.height

state = State()
button_one = Button('[Button 1]', 100, windowHeight-10)
button_two = Button('[Button 2]', 100, (windowHeight-10)-button_one.label().content_height-10)
button_three = Button('[Button 3]', 100, (windowHeight-10)-button_one.label().content_height-10-button_two.label().content_height-10)

@window.event
def on_draw():
    window.clear()
    button_one.render()
    button_two.render()
    button_three.render()

@window.event
def on_key_press(symbol, modifiers):
    button_one.setText('A key was pressed')

@window.event
def on_mouse_motion(x, y, dx, dy):
    if button_one.withinBoundry(x,y):
        button_one.setText('<Button 1>')
    else:
        button_one.setText('[Button 1]')

    if button_two.withinBoundry(x,y):
        button_two.setText('<Button 2>')
    else:
        button_two.setText('[Button 2]')

    if button_three.withinBoundry(x,y):
        button_three.setText('<Button 3>')
    else:
        button_three.setText('[Button 3]')

@window.event
def on_mouse_press(x, y, mouseButton, modifiers):
    if button_one.withinBoundry(x,y):
        button_one.setText('+Button 1+')
    else:
        button_one.setText('[Button 1]')

    if button_two.withinBoundry(x,y):
        button_two.setText('+Button 2+')
    else:
        button_two.setText('[Button 2]')

    if button_three.withinBoundry(x,y):
        button_three.setText('+Button 3+')
    else:
        button_three.setText('[Button 3]')
            
pyglet.app.run()
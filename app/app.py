import pyglet
from pyglet.window import mouse
from .components.button import Button
from .components.menu import Menu
from .state.state import State

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
window = pyglet.window.Window(fullscreen=False)
windowHeight = window.height

#button_one = Button('[Button X]', 100, windowHeight-10, None)
#button_two = Button('[Button B]', 100, (windowHeight-10)-button_one.label().content_height-10, None)
#button_three = Button('[Button C]', 100, (windowHeight-10)-button_one.label().content_height-10-button_two.label().content_height-10)

#print('x was 100, y was ' + str(windowHeight-10))
#print(button_one.x())
#print(button_one.y())

#print('x was 100, y was ' + str((windowHeight-10)-button_one.label().content_height-10))
#print(button_two.x())
#print(button_two.y())

source = pyglet.media.load('./app/music/test2.wav')
source.play()

menu = Menu(100, (windowHeight-30), 'orange')
menu.add_button('[Button 9]', 'green')
menu.add_button('[Button 6]', 'green')
menu.add_button('[Button 7]', 'green')

state = State()
#state.add_component(button_one)
#print(state.get_components()[0])
#state.render_components()

@window.event
def on_draw():
    window.clear()
    #button_one.render()
    #button_two.render()
    #button_three.render()
    menu.render()

#@window.event
#def on_key_press(symbol, modifiers):
#    button_one.setText('A key was pressed')

@window.event
def on_mouse_motion(x, y, dx, dy):
    menu.on_hover(x,y)
    #if button_one.withinBoundry(x,y):
    #    button_one.setText('<Button 1>')
    #else:
    #    button_one.setText('[Button 1]')

    #if button_two.withinBoundry(x,y):
    #    button_two.setText('<Button 2>')
    #else:
    #    button_two.setText('[Button 2]')

    #if button_three.withinBoundry(x,y):
    #    button_three.setText('<Button 3>')
    #else:
    #    button_three.setText('[Button 3]')

@window.event
def on_mouse_press(x, y, mouseButton, modifiers):
    menu.on_click(x,y)
    #if button_one.withinBoundry(x,y):
    #    button_one.setText('+Button 1+')
    #else:
    #    button_one.setText('[Button 1]')

    #if button_two.withinBoundry(x,y):
    #    button_two.setText('+Button 2+')
    #else:
    #    button_two.setText('[Button 2]')

    #if button_three.withinBoundry(x,y):
    #    button_three.setText('+Button 3+')
    #else:
    #    button_three.setText('[Button 3]')

@window.event
def on_mouse_release(x, y, mouseButton, modifiers):
    menu.on_release(x,y)


pyglet.app.run()
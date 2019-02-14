import pyglet
from pyglet.window import mouse

window = pyglet.window.Window(fullscreen=False)
label = pyglet.text.Label('Pyglet Rocks', font_name='Arial', font_size=20, x=window.width//2, y=window.height//2,anchor_x='center',anchor_y='center')
labelb = pyglet.text.HTMLLabel('<font face="Times New Roman" color="white"><font size="200">Some <b>HTML</b> <i>Text</i></font></font>', x=window.width//2, y=(window.height//4)*3,anchor_x='center',anchor_y='center')
labelVal = 'Not moving, not hover'

@window.event
def on_draw():
    global labelVal
    window.clear()
    label.text = labelVal
    label.draw()
    labelb.draw()

@window.event
def on_key_press(symbol, modifiers):
    global labelVal
    labelVal = 'A key was pressed'

@window.event
def on_mouse_motion(x, y, dx, dy):
    global labelVal

    xleft = (label.x - (label.content_width/2))
    xright = (label.x + (label.content_width/2))
    ytop = (label.y - (label.content_height/2))
    ybottom = (label.y + (label.content_height/2))

    if (xright>x>xleft) and (ybottom>y>ytop):
        labelVal = 'Hovering'
    else:
        labelVal = 'Not moving, not hover'

@window.event
def on_mouse_press(x, y, button, modifiers):
    global labelVal

    xleft = (label.x - (label.content_width/2))
    xright = (label.x + (label.content_width/2))
    ytop = (label.y - (label.content_height/2))
    ybottom = (label.y + (label.content_height/2))

    if (xright>x>xleft) and (ybottom>y>ytop):
        labelVal = 'Clicked!'
            
pyglet.app.run()
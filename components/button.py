import pyglet

class Button:
    def __init__(self, text, x, y):
        self.__label = pyglet.text.Label(text, font_name='Arial', font_size=20, x=x, y=y,anchor_x='left',anchor_y='top')

    def setText(self, text):
        self.__label.text = text

    def render(self):
        self.__label.draw()

    def label(self):
        return self.__label

    def withinBoundry(self, x, y):
        x1left = self.__label.x
        x1right = self.__label.x + self.__label.content_width
        y1top = self.__label.y - self.__label.content_height
        y1bottom = self.__label.y
        return (x1right>x>x1left) and (y1bottom>y>y1top)

    def onClick(self, clicked):
        if clicked == True:
            print('Clicked')
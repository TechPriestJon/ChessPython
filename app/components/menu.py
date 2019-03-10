import pyglet
from .button import Button
from .border import Border

class Menu:
    def __init__(self, x, y, background):
        self.__x = x
        self.__y = y
        #self.__image = pyglet.image.load(background)
        #self.__sprite = pyglet.sprite.Sprite(self.__image, x, y - self.__image.height)
        self.__components = []
        self.__border = Border(x -10, y + 5, background)

    def render(self):        
        #self.__sprite.draw()
        for component in self.__components:
            component.render()
        
        self.__border.render(self.__components[-1].width() + 10 + 20, self.__components[-1].height() + 20 + 20)

    #def add_button(self, text):
        #if len(self.__components) > 0:
        #    x = self.__component[-1].x() + 10
        #    y = self.__components[-1].y() - (self.__components[-1].content_height + 10)
        #else:
        #    x = self.__x + 10
        #    y = self.__y - 10

        #button = Button(text, x, y)
        #self.__components.append(button)

    def add_button(self, text, background):
        if len(self.__components) > 0:
            x = self.__component[-1].x() + 10
            y = self.__components[-1].y() - (self.__components[-1].content_height + 10)
        else:
            x = self.__x + 10
            y = self.__y - 10

        button = Button(text, x, y, background)
        self.__components.append(button)

    def withinBoundry(self, x, y):
        x1left = self.__x
        x1right = self.__x + self.__label.content_width
        y1top = self.__y - self.__label.content_height
        y1bottom = self.__y
        return (x1right>x>x1left) and (y1bottom>y>y1top)
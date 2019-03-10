import pyglet
from .border import Border

class Button:
    def __init__(self, text, x, y, background):
        self.__original_text = text
        self.__label = pyglet.text.Label(text, font_name='Arial', font_size=20, x=x, y=y,anchor_x='left',anchor_y='top')
        self.__border = Border(x -10, y + 5, background)
        #if background is not None:
        #    self.__image = pyglet.image.load(background)
        #    self.__sprite = pyglet.sprite.Sprite(self.__image, x, y - self.__label.content_height)

    def setText(self, text):
        self.__label.text = text

    def render(self):
        #while self.__sprite.height > self.__label.content_height:
        #    self.__sprite.scale = self.__sprite.scale - 0.01
        #self.__sprite.draw()
        self.__border.render(self.__label.content_width + 10, self.__label.content_height + 20)
        self.__label.draw()

    def width(self):
        return self.__label.content_width

    def height(self):
        return self.__label.content_height    

    def label(self):
        return self.__label

    def x(self):
        return self.__label.x

    def y(self):
        return self.__label.y

    def withinBoundry(self, x, y):
        x1left = self.__label.x
        x1right = self.__label.x + self.__label.content_width
        y1top = self.__label.y - self.__label.content_height
        y1bottom = self.__label.y
        return (x1right>x>x1left) and (y1bottom>y>y1top)

    def on_hover(self, x, y):
        if self.withinBoundry(x,y):
            self.setText('<Button 1>')
        else:
            self.__reset()


    def on_click(self, x, y):    
        if self.withinBoundry(x,y):
            self.setText('+Button 1+')
        else:
            self.__reset()

    def __reset(self):
        self.setText(self.__original_text)

    def on_release(self, x, y):
        if self.withinBoundry(x,y):
            self.on_hover(x,y)


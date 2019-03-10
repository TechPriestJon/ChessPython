import pyglet

class Border:
    def __init__(self, x, y, graphic):
        self.__x = x
        self.__y = y
        self.__topleft = pyglet.image.load('./app/components/' + graphic + '/topleft.png')
        self.__topright = pyglet.image.load('./app/components/' + graphic + '/topright.png')
        self.__bottomleft = pyglet.image.load('./app/components/' + graphic + '/bottomleft.png')
        self.__bottomright = pyglet.image.load('./app/components/' + graphic + '/bottomright.png')
        self.__horizontal = pyglet.image.load('./app/components/' + graphic + '/horizontal.png')
        self.__vertical = pyglet.image.load('./app/components/' + graphic + '/vertical.png')                                        

    def render(self, width, height):   
        horizontal_units = width / 10
        vertical_units = height / 10

        sprites = []
        sprites.append(pyglet.sprite.Sprite(self.__topleft, self.__x, self.__y))

        sprites.append(pyglet.sprite.Sprite(self.__topright, self.__x + (self.__horizontal.width * horizontal_units), self.__y))
        
        sprite_count = 1
        while sprite_count < horizontal_units:
            sprites.append(pyglet.sprite.Sprite(self.__horizontal, self.__x + (self.__horizontal.width * sprite_count), self.__y))
            sprite_count += 1

        sprite_count = 1
        while sprite_count < vertical_units:
            sprites.append(pyglet.sprite.Sprite(self.__vertical, self.__x, self.__y - (self.__vertical.width * sprite_count)))
            sprite_count += 1

        sprite_count = 1
        while sprite_count < horizontal_units:
            sprites.append(pyglet.sprite.Sprite(self.__horizontal, self.__x + (self.__horizontal.width * sprite_count), self.__y - (self.__vertical.width * vertical_units)))
            sprite_count += 1

        sprite_count = 1
        while sprite_count < vertical_units:
            sprites.append(pyglet.sprite.Sprite(self.__vertical, self.__x + (self.__horizontal.width * horizontal_units), self.__y - (self.__vertical.width * sprite_count)))
            sprite_count += 1

        
        sprites.append(pyglet.sprite.Sprite(self.__bottomleft, self.__x, self.__y - (self.__vertical.width * vertical_units)))

        sprites.append(pyglet.sprite.Sprite(self.__bottomright, self.__x + (self.__horizontal.width * horizontal_units), self.__y - (self.__vertical.width * vertical_units)))


        for sprite in sprites:
            sprite.draw()


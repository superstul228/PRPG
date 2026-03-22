class Game():
    def __init__(self):
        self.scenes = {}

    #initing pygame, creating window, starting main cycle
    def run(self, sizex, sizey, name):
        import pygame as pg
        pg.init()
        self.window = pg.display.set_mode((sizex, sizey))
        pg.display.set_caption(name)

    #decorator for creating scenes
    def Scene(self, name):
        def decorator(cls):
            self.scenes[name] = cls
            return cls
        return decorator

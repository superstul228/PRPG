#THIS IS TEST FILE
from engine import *

game = Game()

@game.Scene("main")
class MainScene():
    def on_enter(self):
        pass
    def on_exit(self):
        pass
    def handle_event(self):
        pass
    def update(self):
        pass

game.run(500, 500, "pisun")

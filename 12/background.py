from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 60)

    def update(self):
        pass
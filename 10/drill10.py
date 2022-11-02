import random
from pico2d import *
import game_framework
import item_state

# Game object class here
class Grass:
    def __init__(self): # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.dir = 1

    def update(self): # 소년 행위 구현
        self.frame = (self.frame +1) % 8
        self.x += self.dir * 5
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# 게임종료 - 객체 소멸
def exit():
    global boy, grass
    del boy
    del grass

def update():
    # 게임 월드 객체 업데이트
    boy.update()

def draw():
    # 게임 월드 렌더링
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)
            #elif event.key == SDLK_+:
            #elif event.key == SDLK_-:


# initialization code
open_canvas()
running = True
enter()
# game main loop code
while running:

    handle_events()
    clear_canvas()
    draw()
    update_canvas()
    delay(0.05)

close_canvas()


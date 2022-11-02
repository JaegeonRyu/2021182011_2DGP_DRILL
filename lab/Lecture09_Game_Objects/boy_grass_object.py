import random
from pico2d import *

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
        self.x += 5   # 속성 값을 바꿔 소년의 행위(오른쪽 이동) 구현
        self.frame = (self.frame +1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass() # 잔디 객체 생성
# boy = Boy() # 소년 객체 생성
# team
team = [ Boy() for i in range(11) ]
running = True

# game main loop code
while running:

    handle_events() # 키 입력을 받아들이는 처리

    # Game logic
    # grass에 대한 상호작용
    for boy in team:
        boy.update() # 소년 상호작용

    # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)

# finalization code


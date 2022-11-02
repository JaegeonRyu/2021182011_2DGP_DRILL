import pico2d
from pico2d import *
import game_framework
import item_state
import title_state
import logo_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.dir = 1
        self.item = 'BigBall'

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)

        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_ESCAPE:
                game_framework.push_state(item_state)

# 게임 초기화: 게임 객체들을 생성
boy = None # c NULL
grass = None

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

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    # 게임 월드 렌더링
    clear_canvas()
    draw_world()
    update_canvas()

def test_self():
    import  sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': # 만약 단독 실행 중이라면
    test_self()

open_canvas()
enter()
# game main loop code
while running:
    handle_events()
    update()
    draw()
    delay(0.01)
exit()
# finalization code
close_canvas()

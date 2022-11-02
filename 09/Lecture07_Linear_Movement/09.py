from pico2d import *
import random
import time

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def render():
    global X, Y

    PointX = random.randint(100, 1100)
    PointY = random.randint(100, 900)
    preX = PointX
    hand.draw(PointX, PointY)
    if PointX < preX:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif PointX > preX:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)




open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    PointX = random.randint(100, 1100)
    PointY = random.randint(100, 900)
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(PointX, PointY)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
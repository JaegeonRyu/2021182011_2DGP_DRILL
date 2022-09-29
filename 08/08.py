from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1200, 800

def handle_events():
    global running
    global dirx
    global diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
Tuk = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 600
y = 400
framex = 0
framey = 9
dirx = 0
diry = 0

while running:
    clear_canvas()
    Tuk.draw(600, 400)
    if dirx >= 0:
        character.clip_draw(framex * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    if dirx <= 0:
        character.clip_draw(framey * 100, 200 * 1, 100, 100, x, y)
    update_canvas()

    handle_events()
    framex = (framex + 1) % 8
    framey = (framey - 1) % 8
    x += dirx * 5
    y += diry * 5

    if x >= 1200:
        x -= dirx * 5
    elif x <= 0:
        x -= dirx * 5
    elif y >= 800:
        y -= diry * 5
    elif y <= 0:
        y = 10
    delay(0.01)

close_canvas()
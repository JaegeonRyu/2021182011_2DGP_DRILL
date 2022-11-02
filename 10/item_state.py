from pico2d import *
import drill10
import game_framework

def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image
    # fill here

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state(drill10)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    # fill here

enter()
open_canvas()
draw()
close_canvas()
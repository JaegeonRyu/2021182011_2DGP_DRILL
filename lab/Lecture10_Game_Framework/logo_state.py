from pico2d import *
import game_framework
import title_state

image = None
runnig = True
logo_time = 0.0

def enter():
    global image, logo_time, runnig
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    runnig = True
    # fill here


def exit():
    global image
    del image
    # fill here

def update():
    global runnig
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
        delay(0.01)
        logo_time += 0.01
    # fill here


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    # fill here


def handle_events():
    events = get_events()






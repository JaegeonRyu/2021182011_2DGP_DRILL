from pico2d import *
open_canvas()
grass = load_image('grass.png')
ani = load_image('ani.png')

x = 0
frame = 0

while (x < 800):

    clear_canvas()
    grass.draw(400, 30)
    ani.clip_draw(frame * 30, 255, 40, 50, 400, 75)
    update_canvas()
    frame = (frame + 1) % 13
    x += 5
    delay(0.06)
    get_events()

    clear_canvas()
    grass.draw(400, 30)
    ani.clip_draw(frame * 10, 350, 50, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 10
    x += 5
    delay(0.06)
    get_events()

close_canvas()
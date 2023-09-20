from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
anim = 0
while (1):
    if anim == 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)
        if x > 750:
            anim = 1
    elif anim == 1:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.001)
        if y > 550:
            anim = 2
    elif anim == 2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.001)
        if x < 50:
            anim = 3
    elif anim == 3:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.001)
        if y < 90:
            anim = 0
        
    

close_canvas()


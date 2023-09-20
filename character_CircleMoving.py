from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

px = 0
py = 0
x = 400
y = 300
r = 200
angle = 100
while (1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    px = x + r * math.cos(math.radians(angle))
    py = y + r * math.sin(math.radians(angle))
    character.draw_now(px, py)
    angle = (angle + 1) % 360
    delay(0.001)
    
    
        
    

close_canvas()


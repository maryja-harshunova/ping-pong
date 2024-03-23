from pygame import *

SCREENSIZE = (700, 700)
BACKCOLOR = (198, 218, 191)

window = display.set_mode(SCREENSIZE)
display.set_caption('ping pong')

timer = time.Clock()

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(BACKCOLOR)
    display.update()
    timer.tick(60)
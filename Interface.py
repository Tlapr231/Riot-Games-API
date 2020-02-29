import sys
import pygame as pg

def runGame() :
    pg.init()
    screenDimension = (1200, 700)
    bgColor = (25, 25, 30)
    screen = pg.display.set_mode(screenDimension)
    screen.fill(bgColor)
    Rect = pg.Rect(100,100, 50, 50)
    color = (100, 20 , 20)
    pg.draw.rect(screen, color, Rect)
    pg.display.set_caption("Green League")

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        pg.display.flip()

runGame()

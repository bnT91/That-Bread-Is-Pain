import pygame as pg
import sys

pg.init()
clock = pg.time.Clock()

anim_cycle = 1
tps = 20

scr = pg.display.set_mode((576, 576))  # 48 * 12
pg.display.set_caption("That Bread Is Pain!")

background = pg.image.load("img/back.png")


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()


while True:
    pg.display.update()

    scr.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(tps)

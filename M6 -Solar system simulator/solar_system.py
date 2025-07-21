#libraries 
import pygame as pg
import math
from random import randint


# intialize pygame 
pg.init()


#Create Window 
screen_info = pg.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW = pg.display.set_mode((WIDTH-150, HEIGHT-150))
pg.display.set_caption('Solar system Simulator')


#Colors 
WHITE = (255, 255, 255)
BLACK =(0,0,0)
# Create a simulation
run=True
while run:
    WINDOW.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
        
    pg.display.update()


# Quit the Pygame
pg.quit()
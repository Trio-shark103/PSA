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
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Solar system Simulator')


#Colors 
WHITE = (255, 255, 255)
BLACK =(0,0,0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
YELLOWISH_WHITE =(255, 255, 246)
BLUE = (0,0, 255)
RED = (188, 39, 50)

# Class for Planetary Bodies
class PlanetaryBodies:

    AU = 1.496e11 # Astronomical unit ( distance from the sun to the earth)
    SCALE = 300/AU


    # constructor 
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.color = color 
        self.x =x
        self.y = y
        self.mass = mass
        self.radius = radius

    
    # Method 1 - draw the bodies on the simulator 
    def draw_body(self, WINDOW):
        x = self.x*PlanetaryBodies.SCALE + WIDTH//2
        y = self.y*PlanetaryBodies.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW,color=self.color,center=(x,y), radius=self.radius)



# Stars List with Color , Cneter and Radius information
stars_list = [
    {
        'color': (randint(190, 255), randint(190,255), randint(190,255)),
        'center': (randint(5, WIDTH-5),randint(5, HEIGHT-5)),
        'radius': (randint(1, 2)) 

    }
    for star in range(450)
]

# Function to draw stars on the pygame window
def draw_stars(stars_list):
    for star in stars_list:
        pg.draw.circle(WINDOW, star['color'], star['center'], star['radius'])


# Create a simulation
run=True

sun = PlanetaryBodies("Sun", YELLOW, 0, 0, 1.989e30, 30 )
mercury=PlanetaryBodies("Mercury", GRAY, 0.39*PlanetaryBodies.AU, 0, 0.33E24, 6 )
venus = PlanetaryBodies("Venus", YELLOWISH_WHITE, 0.72*PlanetaryBodies.AU, 0, 4.87e24, 14)
earth = PlanetaryBodies("Earth", BLUE, 1*PlanetaryBodies.AU, 0, 5.97E24, 15)
mars = PlanetaryBodies("Mars", RED, 1.52*PlanetaryBodies.AU, 0, 0.642e24, 8)


while run:
    WINDOW.fill(BLACK)
    draw_stars(stars_list)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            run=False
    Pl_bodies = [sun, mercury, venus, earth, mars]  
    for body in Pl_bodies:
        body.draw_body(WINDOW)  
    pg.display.update()


# Quit the Pygame
pg.quit()
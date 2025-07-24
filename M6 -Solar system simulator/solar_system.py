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
    SCALE = 300/AU # Scale the size of the body to either big or small
    G = 6.6743e-11 # Gravitational constant
    TIME_STEP = 24*3600 # Convert 24hrs to seconds


    # constructor 
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.color = color 
        self.x =x
        self.y = y
        self.mass = mass
        self.radius = radius
        

        self.x_vel = 0
        self.y_vel = 0
        self.orbit = []

    
    # Method 1 - draw the bodies on the simulator 
    def draw_body(self, WINDOW):
        x = self.x*PlanetaryBodies.SCALE + WIDTH//2
        y = self.y*PlanetaryBodies.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW,color=self.color,center=(x,y), radius=self.radius)

    #Method 2- Calculation for the gravitational force 
    def gravitational_force (self, pl_body):
        # F= GMm/r^2
        x_diff = pl_body.x - self.x
        y_diff = pl_body.y -self.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        g_force = self.G* self.mass * pl_body.mass / distance**2
        theta = math.atan2(y_diff, x_diff)  # atan2 takes in input values and into the account of the directions 
        f_x = g_force*math.cos(theta)
        f_y = g_force*math.sin(theta)

        return f_x, f_y
    
    #Method 3 - Update the Position 
    def update_position(self , pl_bodies):   
        net_fx, net_fy = 0, 0
        for pl_body in pl_bodies:
            if self != pl_body:
                f_x, f_y = self.gravitational_force(pl_body)
                net_fx += f_x
                net_fy += f_y
        self.x_vel += net_fx / self.mass * self.TIME_STEP
        self.y_vel += net_fy / self.mass * self.TIME_STEP
        self.x += self.x_vel * self.TIME_STEP
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y))
            




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

paused=False
sun = PlanetaryBodies("Sun", YELLOW, 0, 0, 1.989e30, 30 )
mercury=PlanetaryBodies("Mercury", GRAY, 0.39*PlanetaryBodies.AU, 0, 0.33E24, 6 )
mercury.y_vel= -47.4e3
venus = PlanetaryBodies("Venus", YELLOWISH_WHITE, 0.72*PlanetaryBodies.AU, 0, 4.87e24, 14)
venus.y_vel = -35e3
earth = PlanetaryBodies("Earth", BLUE, 1*PlanetaryBodies.AU, 0, 5.97E24, 15)
earth.y_vel = -29.8e3
mars = PlanetaryBodies("Mars", RED, 1.52*PlanetaryBodies.AU, 0, 0.642e24, 8)
mars.y_vel = -24.1e3


# Set the Frame Per Second(FPS) for the simulation 
FPS = 60
clock = pg.time.Clock()

while run:
    clock.tick(FPS)
    WINDOW.fill(BLACK)
    draw_stars(stars_list)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run=False
            elif event.key == pg.K_SPACE:
                paused = not paused
    if not paused:   
        Pl_bodies = [sun, mercury, venus, earth, mars]  
        for body in Pl_bodies:
            body.update_position(Pl_bodies)
            body.draw_body(WINDOW)  
        pg.display.update()


# Quit the Pygame
pg.quit()
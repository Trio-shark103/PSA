import pygame as pg 
from colors import *
from parameters import SIMULATION_SCALE
import math

# Class for Planetary Bodies
class SolarSystemBodies:

    AU = 1.496e11 # Astronomical unit ( distance from the sun to the earth)
    SCALE =   SIMULATION_SCALE/AU # Scale the size of the body to either big or small
    G = 6.6743e-11 # Gravitational constant
    TIME_STEP = 24*3600 # Convert 24hrs to seconds


    # constructor 
    def __init__(self, name, color, x, y, mass, simulator_radius, y_vel, sun=False):
        self.name = name
        self.color = color 
        self.x =x*self.AU
        self.y = y
        self.mass = mass
        self.simulator_radius = simulator_radius

        self.sun = sun
        self.distance_to_sun = 0
        

        self.x_vel = 0
        self.y_vel = y_vel
        self.orbit = []

    
    # Method 1 - draw the bodies on the simulator 
    def draw_body(self, WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT):
        x = self.x*self.SCALE + WIDTH//2
        y = self.y*self.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW,color=self.color,center=(x,y), radius=self.simulator_radius)
        if not self.sun:
            name_text = NAME_TEXT.render(self.name, True, NAME_TEXT_COLOR)
            WINDOW.blit(name_text, (x-40, y-50))
            dist_text = DIST_TEXT.render(f"{round(self.distance_to_sun/(3e8*60), 3)}lt-min", True, DIST_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-35))

        else:
            name_text = NAME_TEXT.render(self.name, True, SUN_NAME_COLOR)
            WINDOW.blit(name_text, (x-40, y-80))
            dist_text = DIST_TEXT.render(f"{round(self.x/(3e8), 3), round(self.y/(3e8), 3)}lt-sec", True, DIST_TEXT_COLOR)
            WINDOW.blit(dist_text, (x-40, y-55))
    
    #Method 4 - Track the Orbit
    def _track_orbit(self,WINDOW,WIDTH, HEIGHT):
        if len(self.orbit) > 1:
            centered_points = []
            for (x,y) in self.orbit:
                x = x*self.SCALE + WIDTH//2
                y = y*self.SCALE + HEIGHT//2
                centered_points.append((x,y))
            pg.draw.lines(surface=WINDOW, color=self.color, closed=False, points=centered_points, width=2)

             
    #Method 5 - draw
    def draw(self, WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT, track=True):
        self.draw_body(WINDOW, WIDTH, HEIGHT, NAME_TEXT, DIST_TEXT)
        if track:
            self.track_orbit(WINDOW, WIDTH,HEIGHT)


    #Method 2- Calculation for the gravitational force 
    def gravitational_force (self, solar_system_body):
        # F= GMm/r^2
        x_diff = solar_system_body.x - self.x
        y_diff = solar_system_body.y -self.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        if solar_system_body.sun:
            self.distance_to_sun = distance 
        g_force = self.G* self.mass * solar_system_body.mass / distance**2
        theta = math.atan2(y_diff, x_diff)  # atan2 takes in input values and into the account of the directions 
        f_x = g_force*math.cos(theta)
        f_y = g_force*math.sin(theta)

        return f_x, f_y
    
    #Method 3 - Update the Position 
    def update_position(self , solar_system_bodies):   
        net_fx, net_fy = 0, 0
        for body in solar_system_bodies:
            if self != body:
                f_x, f_y = self.gravitational_force(body)
                net_fx += f_x
                net_fy += f_y
        self.x_vel += net_fx / self.mass * self.TIME_STEP
        self.y_vel += net_fy / self.mass * self.TIME_STEP
        self.x += self.x_vel * self.TIME_STEP
        self.y += self.y_vel * self.TIME_STEP
        self.orbit.append((self.x, self.y))
            





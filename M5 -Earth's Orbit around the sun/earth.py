# Problem Statement
# Create a simulation to track the orbit of the Earth around the Sun for a period of 1 year.

# Use Euler and Runge - Kutta method of 4th order (RK4) for this task.

# Find the distance from Earth to Sun at Apogee using Euler and RK4 method and compare it with the original.

# Given Equations 

# Acc of the earth due to gravity of the sun
# a = (-GM/|r|^3)* r_vec

# Ordinary differnetial equation(ode)  for position
# dr/dt =v

# ode for velecity 
# dr/dt =a

# Itial Cndition
# Earth is at its Perihelion (closest to Sun)

# imports 
import numpy as np 
import matplotlib.pyplot as plt


# Constants
G = 6.6743e-11
M_sun = 1.989e30  # in kg

# Intial position and velocity of the earth
r_0 = np.array([147.1e9, 0])  # m
v_0 = np.array([0, 30.29e3]) #m/s

# Time steps and total time for simulation 
dt = 3600 # secs
t_max = 3.154e7 # secs


# Time  array to be used in numerical solution 
t = np.arange ( 0, t_max , dt) # arrange the time from 0 to value of t_max at an interval of value in dt
print (t.astype('int32'))

# intialize arrays to store positions and velocities at all the time steps
r = np.empty(shape=(len(t), 2))
v = np.empty(shape=(len(t), 2))

# set the initial conditions for position and velocity
r[0], v[0] = r_0 , v_0
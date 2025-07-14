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
v_0 = np.array([0, -30.29e3]) #m/s

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

#Define the function that gets us the accn vector when passeed in the position vector
def accn(r):
     return (-G*M_sun / np.linalg.norm(r)**3) * r

#Euler Integration 
def euler_method(r,v,accn,dt):

     """Ordinary differnetial equation(ode)  for position
     dr/dt =v
     r_new = r_old  + V*dt

     # ode for velecity 
     dr/dt =a
     v_new = v_old  + a (r_old)*dt

     #Parameter
     #r: empty array for position of size t
     #v: empty array for velocity of size t
     #accn: func to calculate the accn at given position
     #dt: time step for the simulation
     This function will update the empty arrays for rand v with the simulated data"""

     for i in range(1, len(t)):
          r[i] = r[i-1] + v[i-1] * dt
          v[i] = v[i-1] + accn(r[i-1]) *dt  
     

# RK4 Integration
def rk4_method(r, v, accn, dt):
     """Ordinary differnetial equation(ode)  for position
     dr/dt =v
     r_new = r_old  + dt/6 (k1r + 2*k2r +2*k3r +k4r)

     # ode for velecity 
     dr/dt =a
     v_new = v_old  + dt/6(k1v +2*k2V +2*k3v +k4v)

     #Parameter
     #r: empty array for position of size t
     #v: empty array for velocity of size t
     #accn: func to calculate the accn at given position
     #dt: time step for the simulation
     This function will update the empty arrays for rand v with the simulated data
     Mrthod to calculate the steps 
     step1: - 0
     k1v = accn(r[i-1])
     k1r = v[i-1]

     step2: - dt/2 using step 1
     k2v = accn(r[i-1] + k1r *dt/2 )
     k2r =  v[i-1] + k1v * dt/2

     step3: - dt/2 using step 2
     k3v =accn(r[i-1] + k2r * dt/2)
     k3r = v[i-1] + k2v * dt/2
      
     step 4 :- dt using step 3
     k4v = accn (r[i-1] + k3r * dt)
     k4r = v[i-1] + k3v * dt

     this function will update the empthy arrays for r and v with the simulated data

     """

     for i in range (1 , len(r)): 
         # step1: - 0
          k1v = accn(r[i-1])
          k1r = v[i-1]

          #step2: - dt/2 using step 1
          k2v = accn(r[i-1] + k1r *dt/2 )
          k2r =  v[i-1] + k1v * dt/2

          #step3: - dt/2 using step 2
          k3v =accn(r[i-1] + k2r * dt/2)
          k3r = v[i-1] + k2v * dt/2
          
          #step 4 :- dt using step 3
          k4v = accn (r[i-1] + k3r * dt)
          k4r = v[i-1] + k3v * dt

          # update the r and v
          v[i] = v[i-1]+ dt/6 * (k1v +2*k2v + 2*k3v + k4v )

          r[i] = r[i-1]+ dt/6 * (k1r +2*k2r + 2*k3r + k4r)

def numerical_integration ( r, v, accn, dt, method= 'euler'):
     """this function will apply the numerical)integratrion based on the method choosen 
     if the method is euler or rk4, the respective method will be implemented
     eles it will raise an error or exception
     Parameters
     #r: empty array for position of size t
     #v: empty array for velocity of size t
     #accn: func to calculate the accn at given position
     #dt: time step for the simulation"""

     if method.lower()== "euler":
          euler_method(r,v,accn,dt)
     elif method.lower()=="rk4":
          rk4_method(r,v,accn,dt)
     else:
          raise Exception (f'You can either choose "euler" or "rk4". Your current input for the method is:- {method}')
     

#call the numerical integration
numerical_integration( r, v, accn , dt , method = 'euler')

# Find the point at which Earth is at its Aphelion ( point at ehich the earth is farthest away from the sun)
sizes = np.array([np.linalg.norm(position) for position in r])
pos_aphelion= np.max(sizes)
arg_aphelion = np.argmax(sizes)
vel_aphelion = np.linalg.norm(v[arg_aphelion])

print(pos_aphelion/1e9, vel_aphelion/1e3)
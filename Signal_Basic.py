# Mostly for Chapter 1 of DSP Book.
#Annotated

#It has Animations !!!!!!!!!!!!
#It has a vertical Phase.
# This is for a cosine function.
#Has time_step Input

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
plt.style.use('dark_background')
plt.rcParams['text.usetex'] = True #Adds latex
import matplotlib.mlab as mlab
import math

fig, (ax0, ax1) = plt.subplots( 2 , 1 ,figsize=(10, 5),layout='constrained') #Just for the window
A = float(input("Amplitude (A): ")) #Amplitude
Fo = float(input("Frequency (Fo): "))#Hertz
v_phase = float(input("Vertical phase: "))
phase = float(input("Phase: "))* math.pi
start_time_ms = float(input("Starting Time(ms): ")) * .001
finish_time_ms = float(input("Finishing Time(ms): ")) * .001 
t_s = float(input("Sampling amount: "))#Sampling value
t = np.arange(start_time_ms, finish_time_ms, t_s)
wo_t = ((2 * np.pi)* Fo) * t
line = A*np.cos(wo_t + phase)+v_phase
line, = ax0.plot(t, line, lw=1, color='#FF7F11') #Draws the line
ax0.axhline(y=0, color="white", linestyle="solid") # For the line at the 0 value in the horizontal (x).
ax0.axvline(x=0,color="white", linestyle="solid") # For the line at the 0 value in the vertical (y).
ax0.set_ylim(-A-v_phase, A+v_phase) #Sets the limit of the box
ax0.set(xlabel='$Time(s)$', ylabel='$Amplitude$',title='$Animation\ of\ A\cos(wo(t)+phase)+vertical\ phase$' )
def animate(i):
    line.set_ydata(A*np.cos(wo_t + phase + i/10)+v_phase)  # update the data.
    return line,
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)
#######################################################################################################################################################################
#This is the static plot
y_t = A * np.cos(wo_t + phase)+ v_phase
ax1.set(xlabel='$Time(s)$', ylabel='$Amplitude$',title='$Static\ A\cos(wo(t)+phase)+vertical\ phase$')
ax1.set_ylim(-A-v_phase,A+v_phase) #Sets the limit of the box
#######################################################################################################################################################################
ax1.axhline(y=0, color="white", linestyle="solid")
ax1.axvline(x=0, color="white", linestyle="solid")
ax1.grid(True, linestyle="dotted") #grid 
ax1.plot(t, y_t, lw=1, color="#F0780F")
plt.show()#Shows the plot
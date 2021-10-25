# This script implements Euler's method for 
# numerically solving first order ODEs.
# You may need to install the matplotlib package.
# Provide the following:
#	x0 - initial x
#	y0 - initial y for that choice of x0
#	n - number of steps in Euler's method
# Define the ODE in the ODE function

from math import *
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

# x_list and y_list store the (x,y) pairs
# that approximate the solution.
# These are for the plot below.

x_list = []
y_list = []

x0 = 0.0
y0 = 1.0
n = 100

x_list.append(x0)
y_list.append(y0)

delta_x = 0.01

# Rewrite ODE in the form y' = f(x,y)
# Return value here is the expression for f(x,y)
def ODE(x, y):
	return -x/y

# This implements Euler's method:
# delta y is approximately y' * delta x
# The successive y values are computed from
# by adding the delta y to the previous y value
def eulers_method(n):
	x = x0
	y = y0
	
	for i in range (1, n+1):
		delta_y = ODE(x, y)*delta_x
		
		x += delta_x
		y += delta_y
		
		x_list.append(x)
		y_list.append(y)

eulers_method(n)

# Plot the (x,y) pairs computed above for
# the approximate solution.
font = {'size' : 20}
matplotlib.rc('font', **font)

euler_plot = plt.plot(x_list, y_list, 'r')
plt.show()

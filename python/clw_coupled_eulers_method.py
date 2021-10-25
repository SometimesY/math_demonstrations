# This script implements Euler's method for 
# numerically solving coupled first order ODEs.
# You may need to install the matplotlib package.
# Provide the following:
#	x0 - collective initial conditions for system
#	delta_t - time step
#	n - number of steps in Euler's method
# Define the ODE in the ODE function

import copy
from math import *
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

# x_list and y_list store the (x,y) pairs
# that approximate the solution.
# These are for the plot below.

t_list = []
x_list = []

x0 = [[3500], [100], [0]]
t0 = 0.0

total_population = 0

for i in range (0, len(x0)):
	total_population += x0[i][0]

# alpha = 0.00385 for current status
# alpha = 0.005 for long term behavior
alpha = .0005/total_population
beta = .003

t_list.append(t0)
x_list = []

for i in range (0, len(x0)):
	x_list.append([0])

for i in range (0, len(x0)):
	x_list[i] = x0[i]

delta_t = 1.0

# Rewrite ODE in the vectorial form x' = f(t,x)
# Return value here is the expression for f(t,x)
def ODE(t, x):
	return [-alpha*x[0][-1]*x[1][-1], alpha*x[0][-1]*x[1][-1] - beta*x[1][-1], beta*x[1][-1]]

# This implements Euler's method:
# delta x is approximately x' * delta_t
# The successive x values are computed from
# by adding the delta t to the previous x value
def eulers_method(n):
	x = copy.deepcopy(x0)
	t = t0
	
	for i in range (0, n):
		for j in range (0, len(x0)):
			x[j][0] += ODE(t, x_list)[j]*delta_t
		
		t += delta_t
		
		t_list.append(t)
		
		for j in range (0, len(x0)):
			x_list[j].append(x[j][0])

eulers_method(24*603)

susceptible = x_list[0]
infected = x_list[1]
recovered = x_list[2]

#print(susceptible)

# Plot the (t,x) pairs computed above for
# the approximate solution.
font = {'size' : 20}
matplotlib.rc('font', **font)

s_plot = plt.plot(t_list, susceptible, 'r')
s_plot = plt.plot(t_list, recovered, 'g')
s_plot = plt.plot(t_list, infected, 'k')
plt.show()

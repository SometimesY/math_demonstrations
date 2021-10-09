# Numerical integrator that uses trapezoidal rule or Simpson's rule based on user selection
# Only need to define:
#	a - left endpoint of integration
#	b - right endpoint of integration
#	n - number of gridpoints
#	f - function to integrate

from math import *

# mode can be trapezoidal or Simpson's
mode = "Simpson's"

if mode not in ("trapezoidal", "Simpson's"):
	exit("Improper integration mode, exiting.")

# left endpoint of integration
a = -1.5

# right endpoint of integration
b = 2.5

# number of grid points
n = 10

# Grid spacing
h = (b-a)/n

# Simpson's rule only works with an even number of gridpoints
if mode == "Simpson's" and n % 2 != 0:
	exit("Simpson's rule requires an even number of grid points, exiting.")

# define our function
def f(x):
	return x*sin(x)

# integration function
def integration():
	# set integral to zero
	integral = 0.0
	
	# add f(a) and f(b) to integral
	# both appear as-is in trapezoidal and Simpson's rules
	integral += f(a)
	integral += f(b)
	
	# do this if the mode is trapezoidal rule
	if mode == "trapezoidal":
		# loop through the points between a = x_0 and b = x_n
		for i in range (1, n):
			# add 2*f(x_i)
			integral += 2.0*f(a + i*h)
		
		# multiply integral by h/2 at the end
		integral *= h/2.0
	# do this if the mode is Simpson's rule
	else:
		# loop through the points between a = x_0 and b = x_n
		for i in range (1, n):
			# if the index (i) on the gridpoint (x_i) is odd, add 4*f(x_i)
			if i % 2 == 1:
				integral += 4.0*f(a + i*h)
			# if the index (i) on the gridpoint (x_i) is even, add 2*f(x_i)
			else:
				integral += 2.0*f(a + i*h)
		
		# multiply integral by h/3 at the end
		integral *= h/3.0
	
	return integral

print(integration())

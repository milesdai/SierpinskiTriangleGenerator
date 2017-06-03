import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

def dist(a,b):
	''' Returns the Euclidian distance between tuples/lists a and b'''
	# a and b must of the same dimensionality
	assert len(a) == len(b)

	distance = 0
	for i in range(len(a)):
		distance += (b[i] - a[i])**2

	return distance ** 0.5

def getDir(a,b):
	''' Returns a list representing the unit direction vector from a to b'''
    # a and b must of the same dimensionality
	assert len(a) == len(b)
	direction = []
	distance = dist(a,b)
	
	for i in range(len(a)):
   		direction.append((b[i] - a[i]) / distance)

	return direction

def make2DTriangle():
	''' Follows an iterative algorithm for generating Sierpinski's Triangle.
	Three reference points define the edges of the triangle. One point is randomly 
	initilized. One of the three vertex points is selected randomly. The midpoint
	between the current point and the vertex point is marked and becomes the new 
	current point. A vertex point is picked at random again, and this process repeated.

	Outputs a plot of Sierpinski's Triangle.
	'''
	
	# Total number of iterations (i.e. points plotted)
	total_iterations = 100000

	# Define outer triangle coordinates
	a = (1,1)
	b = (60,1)
	c = (50,40)
	boundary_points = [a,b,c]

	# Initialize starting point within or on the triangle
	current_point = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]

	# Maintain a list of plotted coordinates
	x_list = [current_point[0]]
	y_list = [current_point[1]]

	iterations = 0

	while iterations < total_iterations:
		# Randomly select a vertex a, b, or c to use as the reference point
		ref_point = boundary_points[random.randint(0, len(boundary_points) - 1)]

		distance = dist(current_point, ref_point)
		direction = getDir(current_point, ref_point)
		displacement = [i * distance / 2 for i in direction]
		
		for i in range(len(displacement)):
			current_point[i] += displacement[i]
		
		x_list.append(current_point[0])
		y_list.append(current_point[1])

		iterations += 1

	plt.plot(x_list, y_list, '.', markersize = 0.5)
	plt.title("{} Iterations".format(total_iterations))
	plt.show()

def make3DTriangle():
	''' Follows an iterative algorithm for generating Sierpinski's Triangle.
	Three reference points define the edges of the triangle. One point is randomly 
	initilized. One of the three vertex points is selected randomly. The midpoint
	between the current point and the vertex point is marked and becomes the new 
	current point. A vertex point is picked at random again, and this process repeated.

	Outputs a plot of Sierpinski's Triangle.
	'''
	
	# Total number of iterations (i.e. points plotted)
	total_iterations = 100

	# Define outer triangle coordinates
	a = (1,1,1)
	b = (60,1,1)
	c = (30,40,50)
	d = (30,60,1)
	boundary_points = [a,b,c,d]

	# Initialize starting point within or on the triangle
	current_point = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (a[2] + b[2]) / 2]

	# Maintain a list of plotted coordinates
	x_list = [current_point[0]]
	y_list = [current_point[1]]
	z_list = [current_point[2]]

	iterations = 0

	while iterations < total_iterations:
		# Randomly select a vertex a, b, or c to use as the reference point
		ref_point = boundary_points[random.randint(0, len(boundary_points) - 1)]

		distance = dist(current_point, ref_point)
		direction = getDir(current_point, ref_point)
		displacement = [i * distance / 2 for i in direction]
		
		for i in range(len(displacement)):
			current_point[i] += displacement[i]
		
		x_list.append(current_point[0])
		y_list.append(current_point[1])
		z_list.append(current_point[2])

		iterations += 1

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	# ax = plt.axes(projection='3d')
	c = [[0.2,0.1,0.7]]#,[0.3,0.3,0.4],[0.4,0.5,0.1]]
	ax.scatter(x_list,y_list,z_list,c=c,s=1)
	plt.title("{} Iterations".format(total_iterations))
	plt.show()

make3DTriangle()

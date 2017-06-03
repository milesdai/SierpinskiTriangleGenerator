import matplotlib.pyplot as plt
import random

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
	
	# Total number of iterations (i.e. points plotted)
	total_iterations = 10000

	# Define outer triangle coordinates
	a = (1,1)
	b = (60,1)
	c = (30,40)
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

make2DTriangle()

# Version of python is python 2.7.12

from OpenGL.GL import *
from OpenGL.GLUT import *

import math
import time
import copy

from thread import start_new_thread

# Initialization of global variable
originX, originY = 250, 250 # Origin value
window = 0  # setting glut window number
width, height = 500, 500  # setting window size
partision = 20  # partision to make animation

# Print the title of the program
print("---<<LINEAR TRANSFORMATION 2D WITH OPENGL>>---")
print("|               - Created By -               |")
print("|       Manasye Shousen Bukit(13516122)      |")
print("|         Regi Arjuna Purba(13516149)        |")
print("----------------------------------------------")

# Inputing the number of points
nbelmt = input("Input number of point : ")

# Initialization of the list needed
vertices = []

# Set the vertices based on users inputs
for counter in range(nbelmt):
	vertices.append([])
	pointsx = input("x[" + str(counter) + "] is : ")
	pointsy = input("y[" + str(counter) + "] is : ") 
	vertices[counter].append(float(pointsx)+float(originX))
	vertices[counter].append(float(pointsy)+float(originY))

vertices2 = copy.deepcopy(vertices) # use module copy to copy all variable inside list

# Function to draw the object
def draw():  

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position

    refresh2d(width, height)
    drawAxis()

    glBegin(GL_POLYGON)
    glColor3f(0,0,1)
    for counter in range(len(vertices)):
        pointx = vertices[counter][0]
        pointy = vertices[counter][1]
        glVertex2f(pointx,pointy)
    glEnd()

    glutSwapBuffers()  # for double buffering

# Function to draw cartesian axis with grid in it
def drawAxis():
	glLineWidth(0.1)
	glColor3f(0.5, 1.0, 0.9)
	wid = 0
	while (wid <= width) :
		len = 0
		while (len <= height) :
			glBegin(GL_LINES)
			glVertex3f(0.0, len, 0.0)
			glVertex3f(wid, len, 0)
			glEnd()
			glBegin(GL_LINES)
			glVertex3f(len, 0, 0.0)
			glVertex3f(len, wid, 0)
			glEnd()
			len += 10
		wid += 50
	
	glLineWidth(2.0)
	wid = 0
	while (wid <= width) :
		len = 0
		while (len <= height) :
			glBegin(GL_LINES)
			glVertex3f(0.0, len, 0.0)
			glVertex3f(wid, len, 0)
			glEnd()
			len += 50
			glBegin(GL_LINES)
			glVertex3f(len, 0, 0.0)
			glVertex3f(len, wid, 0)
			glEnd()
		wid += 50
	
	glLineWidth(1.5)
	glColor3f(0.5, 0.5, 0.5)	
	glBegin(GL_LINES)
	glVertex3f(height/2, 0, 0.0)
	glVertex3f(height/2, width, 0)
	glEnd()
	
	glBegin(GL_LINES)
	glVertex3f(0, width/2, 0.0)
	glVertex3f(height, width/2, 0)
	glEnd()

# Function to do refreshing
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# Function to display the window with images in it
def window() :
    glutInit() # initializing glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height) # set window's size
    glutInitWindowPosition(0, 0) # set window's inital position
    window = glutCreateWindow("Tubes Algeo 2") # create window with title
    glClearColor(1.0, 1.0, 1.0, 1.0) # create a white background
    glutDisplayFunc(draw) # set draw function callback
    glutIdleFunc(draw)	# draw images all the time
    glutMainLoop()	# the loop

# Make a thread so we can input command while having the main drawing loop
start_new_thread(window, ())

# Function to multiply value of two matrixes
def multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
       result.append(0)
       for k in range(len(matrix2)):
           result[i] += matrix1[i][k] * matrix2[k]
    return result

# Function to add value of two matrixes
def add(matrix1, matrix2): 
    result = []
    for i in range(len(matrix1)):
        result.append(matrix1[i] + matrix2[i])
    return result

# Function to do translating
def translate(x,y):
	# The partision
	dx = x/partision
	dy = y/partision
        
    # The loop for animation 
	for j in range(partision):
       	# Partising the coordinate so we can make animation
		matrix_translation = [dx,dy]
        
		for i in range(len(vertices)): 
			vertices[i] = add(vertices[i], matrix_translation)

    	# Time sleep is for postponing the loop
		time.sleep(0.02)	

# Function to do dilating
def dilate(k):
	# The partision
	temp = math.pow(k, 1.0/partision)
	
	# The loop for animation
	for j in range(partision):
		matrix_dilation = [[temp,0],[0,temp]]

		for i in range(len(vertices)):

        	# Substracting the vertices with (0,0) so we can get the real x and y
			vertices[i][0] -= originX
			vertices[i][1] -= originY

			vertices[i] = multiply(matrix_dilation, vertices[i])

            # Adding the vertices with (0,0) so we can turn back x and y
			vertices[i][0] += originX
			vertices[i][1] += originY

        # Time sleep is for postponing the loop
		time.sleep(0.02)

# Function to do rotating counter-clockwise
def rotate(deg,x,y):
	# The partision
	deg = deg/partision

 	# The loop for animation
	for j in range(partision):

        # Move the rotation axis so x,y is the center
		matrix_translation = [-x,-y]
		for i in range(len(vertices)): 
			vertices[i] = add(vertices[i], matrix_translation)

		rad = math.radians(deg)
		matrix_rotation = [[math.cos(rad), -1*math.sin(rad)], [math.sin(rad), math.cos(rad)]]

		for i in range(len(vertices)):
            # Substracting the vertices with (0,0) so we can get the real x and y
			vertices[i][0] -= originX
			vertices[i][1] -= originY

			vertices[i] = multiply(matrix_rotation, vertices[i])

           	# Adding the vertices with (0,0) so we can turn back x and y
			vertices[i][0] += originX
			vertices[i][1] += originY

        # Move back to the real point
		matrix_translation = [x,y]
		for i in range(len(vertices)): #looping as much as number of vertex
			vertices[i] = add(vertices[i],matrix_translation)

        # Time sleep is for postponing the loop  
		time.sleep(0.02) 

# Function to do reflecting other than (a,b)
def reflect(parameter):
	if parameter == 'x':
		matrix_reflection = [[1.0,0.0], [0.0,-1.0]]
	elif parameter == 'y':
		matrix_reflection = [[-1.0,0.0], [0.0,1.0]]
	elif parameter == 'y=x':
		matrix_reflection = [[0.0,1.0], [1.0,0.0]]
	elif parameter == 'y=-x':
		matrix_reflection = [[0.0,-1.0], [-1.0,0.0]]

	temp = copy.deepcopy(vertices) # temp used for storing the changes of each reflection
	for i in range(len(vertices)):

	    # Substracting the vertices with (0,0) so we can get the real x and y
		temp[i][0] -= originX
		temp[i][1] -= originY

		temp[i] = multiply(matrix_reflection, temp[i])

	    # Adding the vertices with (0,0) so we can turn back x and y
		temp[i][0] += originX
		temp[i][1] += originY

	    # Temp store the change causes by partision reflecting
		temp[i][0] = (temp[i][0] - vertices[i][0])/float(partision)
		temp[i][1] = (temp[i][1] - vertices[i][1])/float(partision)
			
	# The loop for animation
	for j in range(partision):
		for i in range(len(vertices)):
			vertices[i][0] += temp[i][0]
			vertices[i][1] += temp[i][1]
        # Time sleep is for postponing the loop
		time.sleep(0.02)	

# Function to do reflecting (a,b)
def reflect2(parameter):
	def is_number(string):
			try:
				float(string)
				return True
			except ValueError:
				return False

	s = list(parameter)

	# s[0] = '('
	# s[1] - s[next] = 'a'
	# s[next+1] = ','
	# s[next+2] - s[s.length-1] = 'b'
	# s[s.length] = ')'

	a = 0  
	next = 0
	for i in range (1,len(s)):
		if(is_number(s[i])):
			a = a * 10 + float(s[i])
			next += 1
		else:
			break
		
	b = 0
	for i in range (next+2,len(s)-1):
		b = b * 10 + float(s[i])

	matrix_reflection = [(2*a),(2*b)]
	temp = copy.deepcopy(vertices)
	for i in range(len(temp)):
           	
    	# Substracting the vertices with (0,0) so we can get the real x and y
		temp[i][0] -= originX
		temp[i][1] -= originY

		temp[i][0] *= -1
		temp[i][1] *= -1

		temp[i] = add(matrix_reflection ,temp[i])

        # Adding the vertices with (0,0) so we can turn back x and y
		temp[i][0] += originX
		temp[i][1] += originY

        # Temp store the change causes by partision reflecting
		temp[i][0] = (temp[i][0] - vertices[i][0])/float(partision)
		temp[i][1] = (temp[i][1] - vertices[i][1])/float(partision)

    # The loop for animation
	for j in range(partision):
		for i in range(len(vertices)):
			vertices[i][0] += temp[i][0]
			vertices[i][1] += temp[i][1]
        # Time sleep is for postponing the loop
		time.sleep(0.02)
    		
# Function to do shearing
def shear(parameter,k):
	test = True
	if parameter == 'x':
		matrix_shearing = [[1,k/partision], [0,1]]
	elif parameter == 'y':
		matrix_shearing = [[1,0], [k/partision,1]]
	else :
		print("You're inputting wrong parameter !")
		test = False
	
	if(test == True):	
	    # The loop for animation
		for j in range(partision):
			for i in range(len(vertices)):
	            # Substracting the vertices with (0,0) so we can get the real x and y
				vertices[i][0] -= originX
				vertices[i][1] -= originY

				vertices[i] = multiply(matrix_shearing, vertices[i])

	            # Adding the vertices with (0,0) so we can get the real x and y
				vertices[i][0] += originX
				vertices[i][1] += originY
	        # Time sleep is for postponing the loop
			time.sleep(0.02)

# Function to do stretching
def stretch(parameter,k):
	# The partision
	temp = math.pow(k, 1.0/partision)
	test = True

	if parameter == 'x':
		matrix_stretch = [[temp,0], [0,1]]
	elif parameter == 'y':
		matrix_stretch = [[1,0], [0,temp]]
	else :
		print("You're inputting wrong parameter !")
		test = False

	if(test == True):
		# The loop for animation
		for j in range(partision):

			for i in range(len(vertices)):

	        	# Substracting the vertices with (0,0) so we can get the real x and y
				vertices[i][0] -= originX
				vertices[i][1] -= originY

				vertices[i] = multiply(matrix_stretch, vertices[i])

	            # Adding the vertices with (0,0) so we can turn back x and y
				vertices[i][0] += originX
				vertices[i][1] += originY

	        # Time sleep is for postponing the loop
			time.sleep(0.02)

# Function to do customing
def custom(a,b,c,d):

	if((a*d)-(b*c) != 0):
		matrix_custom =[[a,b], [c,d]] 
		temp = copy.deepcopy(vertices) # temp used for storing the changes of customization
		for i in range(len(vertices)):

	        # Substracting the vertices with (0,0) so we can get the real x and y
			temp[i][0] -= originX
			temp[i][1] -= originY

			temp[i] = multiply(matrix_custom, temp[i])

	        # Adding the vertices with (0,0) so we can turn back x and y
			temp[i][0] += originX
			temp[i][1] += originY

	        # Temp store the change causes by partision reflecting
			temp[i][0] = (temp[i][0] - vertices[i][0])/float(partision)
			temp[i][1] = (temp[i][1] - vertices[i][1])/float(partision)
			
		# The loop for animation
		for j in range(partision):
			for i in range(len(vertices)):
				vertices[i][0] += temp[i][0]
				vertices[i][1] += temp[i][1]

	        # Time sleep is for postponing the loop
			time.sleep(0.02)

	else :
		# Case where matrx_custom is matrix singular
		print("The determinant of custom matrix must not be 0 !")

# Function to do resetting
def reset():

	temp = copy.deepcopy(vertices2) # temp used for storing the changes of resetting
	# Dividing it into small fragment of transition
	for i in range(len(vertices)):
		temp[i][0] = (temp[i][0]-vertices[i][0])/float(partision)
		temp[i][1] = (temp[i][1]-vertices[i][1])/float(partision)

	# The loop for animation
	for j in range(partision):
		for i in range(len(vertices)):
			vertices[i][0]+=temp[i][0]
			vertices[i][1]+=temp[i][1]
		time.sleep(0.02)

# Inputing the command and split it so we can later use each string as an instruction
command = raw_input().split()

while(True):
	# Action for translating
	if command[0] == 'translate':
		translate(float(command[1]),float(command[2]))

	# Action for dilating	
	elif command[0] == 'dilate':
		dilate(float(command[1]))      

	# Action for rotating
	elif command[0] == 'rotate':
		rotate(float(command[1]),float(command[2]),float(command[3]))

	# Action for reflecting
	elif command[0] == 'reflect':
		parameter = command[1]
		if ((parameter == 'x') or (parameter == 'y') or (parameter == 'y=x') or (parameter =='y=-x')):
			reflect(parameter)
		else :
			reflect2(parameter)

	# Action for shearing
	elif command[0] == 'shear':
		shear(command[1], float(command[2]))

	# Action for stretching
	elif command[0] == 'stretch':
		stretch(command[1], float(command[2]))

	# Action for customing
	elif command[0] == 'custom':
		custom(float(command[1]),float(command[2]),float(command[3]),float(command[4]))

	# Action for multiple action
	elif command[0] == 'multiple':
		N = int(command[1])
		cmd_inside = []

		# Looping through each line and get the command
		for i in range(N):
			cmd = raw_input().split()
			cmd_inside.append(cmd)

		for i in range(N):
			# Action for translating
			if cmd_inside[i][0] == 'translate':
				translate(float(cmd_inside[i][1]), float(cmd_inside[i][2]))

			# Action for dilating
			elif cmd_inside[i][0] == 'dilate':
				dilate(float(cmd_inside[i][1]))

			# Action for rotating
			elif cmd_inside[i][0] == 'rotate':
				rotate(float(cmd_inside[i][1]), float(cmd_inside[i][2]), float(cmd_inside[i][3]))

			# Action for reflecting
			elif cmd_inside[i][0] == 'reflect':
				parameter = cmd_inside[i][1]
				if ((parameter == 'x') or (parameter == 'y') or (parameter == 'y=x') or (parameter =='y=-x')):
					reflect(parameter)
				else :
					reflect2(parameter)

			# Action for shearing
			elif cmd_inside[i][0] == 'shear':
				shear(cmd_inside[i][1], float(cmd_inside[i][2]))

			# Action for stretching
			elif cmd_inside[i][0] == 'stretch':
				stretch(cmd_inside[i][1], float(cmd_inside[i][2]))

			# Action for customing
			elif cmd_inside[i][0] == 'custom':
				custom(float(cmd_inside[i][1]),float(cmd_inside[i][2]),float(cmd_inside[i][3]),float(cmd_inside[i][4]))

			# Action for wrong command
			else :
				print ("You're inputting wrong command!")

	# Action for reseting
	elif command[0] == 'reset':
		reset()

	# Action for exitting
	elif command[0] == 'exit':
		# Print the title of the program
		print("----------------------------------------------")
		print("|        Thanks for using this program       |")
		print("|       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      |")
		print("|              See you next time             |")
		print("----------------------------------------------")
		os._exit(1) # exits the program without calling cleanup handlers, flushing stdio buffers, etc

	# Action for wrong command
	else :
		print ("You're inputting wrong command!")
        
    # Inputing the command and split it so we can later use each string as an instruction
	command = raw_input().split()
   
import numpy as np
import matplotlib.pyplot as plt

def Parabolic(title,x,y, xBorders,yBorders,pos,sorting = ''):
	'''
	Construct a graph with approximate curve using Parabolic algorithm
	'''
	sumx2 = sumx = sumxy = sumy = sumx3 = sumx4 = sumx2y = 0

	x = x.copy()
	y = y.copy()

	if sorting == 'sort':
		x.sort()
		y.sort()
		sorting = ''

	if len(x) == len(y):
		for i in range(0,len(x)):
			sumx += (x[i])
			sumx2 += (x[i]**2)
			sumx3 += (x[i]**3)
			sumx4 += (x[i]**4)
			sumy += (y[i])
			sumxy += (x[i] * y[i])
			sumx2y += ((x[i]**2) * y[i])


	array1 = np.array([[sumx4, sumx3, sumx2],[sumx3, sumx2, sumx], [sumx2, sumx, len(x)]], int)
	array2 = np.array([[sumx2y],[sumxy],[sumy]], int)

	arr = np.dot(np.linalg.inv(array1),array2)

	a = round(arr[0][0],3)
	b = round(arr[1][0],3)
	c = round(arr[2][0],3)

	print('Parabolic Y Function: y='+str(a)+'*x^2+'+str(b)+'*x+' + str(c))

	parabolicX = np.array([*range(0,max(x)+1)],int)
	parabolicY = a*parabolicX**2+b*parabolicX+c

	ConstructGraph(title,x,y,'ro',parabolicX,parabolicY,'g-',xBorders,yBorders,pos)


def Linear(title,x,y,xBorders,yBorders,pos,sorting =''):
	'''
	Construct a graph with approximate curve using Linear algorithm
	'''
	sumx2 = sumx = sumxy = sumy = sumx3 = sumx4 = sumx5 = sumx6 = sumx3y= sumx2y = 0



	for i in range(0,len(x)):
		sumx += (x[i])
		sumx2 += (x[i]**2)
		sumx3 += (x[i]**3)
		sumx4 += (x[i]**4)
		sumx5 += (x[i]**5)
		sumx6 += (x[i]**6)
		sumy += (y[i])
		sumxy += (x[i] * y[i])
		sumx2y += ((x[i]**2) * y[i])
		sumx3y += ((x[i]**3) * y[i])

	array1 = np.array([[sumx2, sumx], [sumx, len(x)]], int)
	array2 = np.array([[sumxy],[sumy]], int)

	arr = np.dot(np.linalg.inv(array1),array2)
	print(arr)

	a = round(arr[0][0],3)
	b = round(arr[1][0],3)

	print('Linear Y Function: y='+str(a)+'*x+'+str(b))


	linearX = np.array([*range(0,max(x)+1)],int)
	linearY = a*linearX+b

	ConstructGraph(title,x,y,'ro',linearX,linearY,'g-',xBorders,yBorders,pos)

def Сube(title,x,y,xBorders,yBorders,pos,sorting =''):
	'''
	Construct a graph with approximate curve using Cube algorithm
	'''
	sumx2 = sumx = sumxy = sumy = sumx3 = sumx4 = sumx5 = sumx6 = sumx3y= sumx2y = 0

	x = x.copy()
	y = y.copy()
	if sorting == 'sort':
		x.sort()
		y.sort()

	for i in range(0,len(x)):
		sumx += (x[i])
		sumx2 += (x[i]**2)
		sumx3 += (x[i]**3)
		sumx4 += (x[i]**4)
		sumx5 += (x[i]**5)
		sumx6 += (x[i]**6)
		sumy += (y[i])
		sumxy += (x[i] * y[i])
		sumx2y += ((x[i]**2) * y[i])
		sumx3y += ((x[i]**3) * y[i])

	array1 = np.array([[sumx6, sumx5, sumx4, sumx3],[sumx5, sumx4, sumx3, sumx2],[sumx4, sumx3, sumx2, sumx], [sumx3, sumx2, sumx, len(x)]], int)
	array2 = np.array([[sumx3y] ,[sumx2y],[sumxy],[sumy]], int)

	arr = np.dot(np.linalg.inv(array1),array2)
	print(arr)

	a = round(arr[0][0],3)
	b = round(arr[1][0],3)
	c = round(arr[2][0],3)
	d = round(arr[3][0],3)

	print('Cube Y Function: y='+str(a)+'*x^3+'+str(b)+'*x^2'+str(c)+'*x'+str(d))


	cubeX = np.array([*range(min(x),max(x)+1)],int)
	cubeY = a*cubeX**3+b*cubeX**2+c*cubeX+d

	ConstructGraph(title,x,y,'ro',cubeX,cubeY,'g-',xBorders,yBorders,pos)



def ConstructGraph(title,x,y,color1, methX, methY, color2,xBorders,yBorders,pos):
	'''
	Builds a Graph with 2 params
	'''

	ax = plt.subplot(pos)
	ax.set_title(title)
	plt.plot(x, y, color1, methX,methY ,color2)
	plt.axis([xBorders['min'],xBorders['max'],yBorders['min'],yBorders['max']])

	plt.ylabel('y')
	plt.xlabel('x')
	

def ShowPlot():
	
	plt.show()


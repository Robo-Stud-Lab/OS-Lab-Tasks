	
#import matplotlib
import numpy as np
import math as m
from random import randint
import const, sheet,itertools,threading,time,sys, graph

def getBorders(axis):
	'''
	Absorbs user input for argument axis, checks it and send to the processing
	'''
	while True:
		Borders = input("\nPlease, input minimum and maximum borders of "+str(axis)+" values(separated with space or comma): ")
	
		Borders = Borders.split(',')
		if len(Borders) == 1: Borders = Borders[0].split(' ')
		
		try:
			for i in range(0,len(Borders)):
				Borders[i] = int(Borders[i])

		except:
			print('Your input doesn\'t seem to be number  :( \n Please, try again\n')
			continue 

		if len(Borders) == 2: 
			if Borders[0] >= Borders[1]: print("Error: Minimum "+str(axis)+" value is bigger than maximum \n")
			elif Borders[1] - Borders[0] <= const.N:
				print("Error: Difference between minimum and maximum must be at least equal to N (N = "+str(const.N))
			else: break

		else: print("Error: Input is incorrect, please, insert TWO numbers with certain separator \n")

	if len(Borders) == 2:
		return Borders


def setBorders(axis):
	'''
	Exports absorbed borders to upcoming cycle
	'''
	appropriate = False

	while True:
		if appropriate == False:
			Borders = getBorders(axis)

		response = input("You set "+axis+" minimum border = "+str(Borders[0])+" and "+axis+" maximum border = "+str(Borders[1])+"\n Is that correct (Y/n)? ")

		if response.lower() == ('y' or 'yes' or 'да'): break
		elif response.lower() == ('n' or 'no' or 'нет'):
			print("Please, insert numbers again...")

		else: 
			appropriate = True
			print('\nYour answer should be \'y\' for yes or \'n\' for yes')

	return Borders	


#cordinates
xyz = [[],[]]
X = setBorders('X')
xBorders = {'min': X[0],'max': X[1]}

Y = setBorders('Y')
yBorders = {'min': Y[0],'max': Y[1]}



def TakeAxis(arr = xyz):
	'''
	Generates N number of points in xyz[]
	'''

	for i in range(0,const.N):
		while True:
			dX = randint(xBorders['min'],xBorders['max'])
			dY = randint(yBorders['min'],yBorders['max'])
			
			if (dX not in arr[0]) and (dY not in arr[1]):
				arr[0].append(dX)#np.append(arr[0],dX)
				arr[1].append(dY)#np.append(arr[1],dY)
				break
	
	return arr				


def animate():
	'''
	Makes a simple animation while loading 
	'''
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		sys.stdout.write('\rFilling in Google Sheet... ' + c)
		sys.stdout.flush()
		time.sleep(0.1)
	


xyz = TakeAxis()
sheet.PurgeSheet()


done = False
t = threading.Thread(target=animate)
t.start()
tic = time.time()

sheet.UpdateSheetByArray(xyz) #.tolist()

toc = time.time()

done = True





print("\nFilling the sheet in took "+str(round(toc-tic, 1))+" secs\n")

graph.Linear('Linear algorithm',xyz[0],xyz[1],xBorders,yBorders,231,'')
graph.Linear('Sorted Linear algorithm',xyz[0],xyz[1],xBorders,yBorders,234,'sort')

graph.Parabolic('Parabolic algorithm',xyz[0],xyz[1],xBorders,yBorders,232)
graph.Parabolic('Sorted Parabolic algorithm',xyz[0],xyz[1],xBorders,yBorders,235,'sort')

graph.Сube('Cube algorithm',xyz[0],xyz[1],xBorders,yBorders,233,'')
graph.Сube('Sorted Cube algorithm',xyz[0],xyz[1],xBorders,yBorders,236,'sort')

graph.ShowPlot()

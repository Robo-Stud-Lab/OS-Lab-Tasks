from Table import *
from random import randint
import numpy as np


Data = Table(0,5000)

amount = 10 #How many elements to be deleted
for i in range(0,amount):
	x = randint(1,Data.N)
	y = randint(1,Data.N)
	Data.removeCell(x,y)

Data.saveMatrix()
Data.viewMatrix("Original Matrix")

Data.winsore('yes')
Data.viewMatrix("Winsored Matrix")

Data.loadMatrix()
Data.linearApprox('yes')
Data.viewMatrix("Linear Approximated Matrix")

Data.loadMatrix()
Data.correlationApprox('yes')
Data.viewMatrix('Correlation Approximation Matrix')
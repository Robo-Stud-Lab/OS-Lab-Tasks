import numpy as np
from random import randint,choice
import math as m
from pandas import DataFrame

class Table:

	N = m.ceil(m.sqrt(3)*10)

	def __init__(self,rMin,rMax):
		'''
		Creates NxN matrix filled with random numbers from rMin to rMax
		'''
		self.matrix = np.random.randint(rMin,rMax, (self.N, self.N))
		self.matrix = self.matrix.astype(object)
		self._original = self.matrix
		self._save = self.matrix


	def saveMatrix(self):
		self._save = np.copy(self.matrix)


	def getCell(self,x,y):
		return str(self.matrix[y,x])


	def removeCell(self,x,y):
		self.changeCell(x,y, np.nan)


	def loadMatrix(self):
		self.matrix = np.copy(self._save)



	def viewMatrix(self,title=''):
		'''
		Makes a nice style for Matrix
		'''
		print("\n")
		print('\x1b[6;33;44m'+title+": "+'\x1b[0m')
		print(DataFrame(self.matrix))
		print("\n")


	def changeCell(self,x,y,value):
		'''
		Changes certain cell of the table
		'''
		try:
			if type(value) != type(np.nan):
				value = int(value)

		except:
			self.throwError('Value is not integer')
			return False

		self.matrix[y-1][x-1] = value
		return True


	def linearApprox(self, showChanged='no'):
		'''
		Approximates missed data with linear approach
		'''
		ChangedElements = [] # Consists of 4 subelements: [1&2] what was and [3&4] > what become

		for y in range(0, self.N):
			for x in range(0, self.N):
				if np.isnan(self.matrix[y,x]):
					
					ChangedElements.append([[x,y]])

					Average = 0
					for ia in range(0,len(self.matrix[y][:x+1])):
						if not np.isnan(self.matrix[y][ia]):
							Average += self.matrix[y][ia]

					self.changeCell(x+1,y+1, round(Average/(x+1)) )

		if showChanged == 'yes': self.__ParseChanged('linear',ChangedElements)
		return self.matrix


	def winsore(self, showChanged='no'):
		'''
		Ressurects elements via winsoring
		'''
		ChangedElements = [] # Consists of 4 subelements: [1&2] what was and [3&4] > what become

		for y in range(0,len(self.matrix)):
			for x in range(0,len(self.matrix[0])):

				if np.isnan(self.matrix[y,x]):
					if not np.isnan(self.matrix[y,x-1]) and x-1 >=0:
						
						ChangedElements.append([[x,y],['previous']])
						self.changeCell(x+1,y+1,self.matrix[y,x-1])

					else:
						if not np.isnan(self.matrix[y,x+1]) and x+1 <= len(self.matrix[0]):
							
							ChangedElements.append([[x,y],['next']])
							self.changeCell(x+1,y+1,self.matrix[y,x+1])
						
						else:
							ChangedElements.append([[x,y],['anomal']])
							w_matrix = -999
		
		if showChanged == 'yes': self.__ParseChanged('winsore',ChangedElements)
		return self.matrix



	def correlationApprox(self,showChanged='no'):

		n = input('Через пробел введите номера восстанавливаемого рядов : ')
		nlist = [int(i) for i in n.split(' ')]
		m = input('Введите номера рядов, с которыми они коррелируют: ')
		mlist = [int(i) for i in m.split(' ')]
		m = mlist

		matrix = self.matrix

		im = 0 

		for n in nlist:
			for j in range(0, self.N):
				if np.isnan(matrix[j,n]) and j == 0:
					value = matrix[j+1,n]/ matrix[j,m[im]]*matrix[j+1,m[im]]
					matrix[j,n] = value
				
				elif np.isnan(matrix[j,n]):
					value = matrix[j-1,n] / matrix[j,m[im]]*matrix[j-1,m[im]]
					matrix[j,n] = value
			im +=1

		return self.matrix

	def __ParseChanged(self,ApprType,ChangedElements):
		'''
		Prints All Changed Elements
		'''
		print("")

		if ApprType == 'winsore':			
			print('\33[46m'+'Winsoring Algorythm Dump: '+'\33[0m')
			for Element in ChangedElements:
				print(str(Element[0])+" was deleted: it is changed with the "+str(Element[1][0])+" value in the line: \33[92m"+self.getCell(*Element[0])+'\33[0m')

		elif ApprType == "linear":
			print('\33[46m'+'Linear Algorythm Dump: '+'\33[0m')
			for Element in ChangedElements:
				print(""+str(Element[0])+" was deleted: it is changed with the approximate value in the line: \33[92m"+self.getCell(*Element[0])+'\33[0m')


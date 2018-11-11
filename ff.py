#!/usr/env python

def transp (A): # транспонирование матрицы 
	n = len(A) 
	m = len(A[0]) 
	trp = [] 
	for i in range(m): 
		trp.append([0] * n) 
	for i in range(m): 
		for j in range(n): 
			trp[i][j] = A[j][i] 
	return trp 

def mult (A1, A2): # Умножение матриц 
	n = len(A1) 
	m = len(A2[0]) 
	res = [] 
	if (len(A1[0]) == len(A2)): 
		for i in range(n): 
			res.append([0] * m)
		for i in range(n): 
			for j in range(m): 
				for k in range(len(A2)): 
					res[i][j] += A1[i][k]*A2[k][j] 
		return res 
	else: 
		print("mult is impossible") 


def sm (A1, A2): # сложение матриц 
	res = [[0,0,0],[0,0,0],[0,0,0]] 
	for i in range(len(A1)):
		for j in range(len(A1[0])): 
			res[i][j]+= A1[i][j]-A2[i][j] 
	return res 


def inv (A): #союзная транспонированная матрица
	AA=[[0,0,0],[0,0,0],[0,0,0]] 
	AA[0][0]+=A[1][1]*A[2][2]-A[1][2]*A[2][1]
	AA[0][1]+=-A[1][0]*A[2][2]+A[2][0]*A[1][2]
	AA[0][2]+=A[1][0]*A[2][1]-A[1][1]*A[2][0]
	AA[1][0]+=-A[0][1]*A[2][2]+A[2][1]*A[0][2]
	AA[1][1]+=A[0][0]*A[2][2]-A[0][2]*A[2][0]
	AA[1][2]+=-A[0][0]*A[2][1]+A[2][0]*A[0][1]
	AA[2][0]+=A[0][1]*A[1][2]-A[1][1]*A[0][2]
	AA[2][1]+=-A[0][0]*A[1][2]+A[1][0]*A[0][2]
	AA[2][2]+=A[0][0]*A[1][1]-A[1][0]*A[0][1]
	AA=transp(AA)
	return AA


def opted (A):	#определитель матрицы
	det=A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
	return det
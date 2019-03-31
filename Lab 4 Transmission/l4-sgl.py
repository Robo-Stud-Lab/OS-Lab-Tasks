#!/usr/env python
import random
import matplotlib.pyplot as plt
import matplotlib as mpl


Y=[]
Y.append([random.randint(0,40) for i in range(50)])
x=[]
x.append([0.1*i for i in range(50)]) 
x1=[]
x1.append([0.1*i for i in range(50)]) 
x1[0].remove(0)
x1[0].remove(1)

def scs(Y): #расчёт скользящего среднего
	Ys=[]
	a=0
	for i in range(2,50):
		for j in range(i-1):
			a+=Y[0][j]
		a=a/(i-1)
		Ys.append(a)
		a=0
	return Ys


def wscs(Y): # расчёт взвешеного скользящего среднего
	Yws=[]
	a=0
	#print(Yws[0],'ys0')
	for i in range(2,50):
		for j in range(i-1):
			a+=Y[0][j]*j
		a=(2*a)/((i-1)*i)	
		Yws.append(a)
		a=0
	return Yws


def es(Y): # экспоненциальное сглаживание
	Ye=[]
	a=0
	Ye.append(Y[0][0])
	alf=0.1
	for i in range(1,50):
		a=alf*Y[0][i]+(1-alf)*Ye[i-1]
		Ye.append(a)
	return Ye

def sg(Y): #расчёт 4го метода
	Yg=[]
	Yg.append(Y[0][0])
	for i in range(1,50):
		a=Y[0][i-1]
		Yg.append(a)
	return Yg


Ys=scs(Y)
Yws=wscs(Y)
Ye=es(Y)
Yg=sg(Y)

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})
plt.axis([0, 6, -1, 45])
plt.title('Сглаживания')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.plot(x[0], Y[0], color = 'blue', linestyle = 'solid', label = 'Сигнал')
plt.plot(x1[0], Ys, color = 'green', linestyle = 'solid', label = 'Скользящее среднее')
plt.plot(x1[0], Yws, color = 'red', linestyle = 'solid', label = 'Взвешеное Скользящее среднее')
plt.plot(x[0], Ye, color = 'black', linestyle = 'solid', label = 'Экспоненциальное взвешивание')
plt.plot(x[0], Yg, color = 'brown', linestyle = 'solid', label = '4й метод')
plt.legend(loc = 'upper right')
plt.show()
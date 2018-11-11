#!/usr/env python
import numpy
import random
import ff
import sympy


			#расчёт передаточной функции

	#матрицы со случайными параметрами
A=[]
for i in range(3):
	A.append([random.randint(-10,10) for j in range(3)])
B=[]
for i in range(3):
	B.append([random.randint(-10,10)])

C=[]
C.append([random.randint(-10,10) for i in range(3)])

print(A,'A')
print(B,'B')
print(C,'C')

s=sympy.symbols('s')# вводим символьную переменную - оператор диффиренцирования
I=[[s,0,0],[0,s,0],[0,0,s]]# единичная матрица*s
ws=[]
det=sympy.factor(ff.opted(ff.sm(I,A)))# знаменатель передаточной функции/хар полином


ws=sympy.factor(ff.mult((ff.mult(C,ff.inv(ff.sm(I,A)))),B))# числитель передаточной функции
print(ws[0][0],'/',det,'передаточная функция')# выводим передаточную функцию


	# находим корни знаменателя/полинома и приводим в адекватный вид
rd=[]
rd=sympy.solve(det)
for i in range(len(rd)):
	rd[i]=complex(rd[i])
#print(rd,'roots of denumenator')


	#находим корни числителя и приводим в адекватный вид
rch=[]
rch=sympy.solve(ws[0][0])
for i in range(len(rch)):
	rch[i]=complex(rch[i])
#print(rch,'roots of numenator')


	#проверяем на возможность сокращения передаточной функции, сравнивая корни полиномов
k=0
for i in range(len(rd)):
	for j in range(len(rch)):
		if (rd[i]==rch[j]):
			print('проблемы с управляемостью/наблюдаемостью')
			k+=1
if (k==0):
	print('нет проблемы с управляемостью/наблюдаемостью')



				#проверка на устойчивость

#массив с реальными частями корней хар полинома
rd1=[]
for i in range(len(rd)):
	a=rd[i]
	rd1.append(a.real)
print(rd1,'реальные части корней хар полинома')


#проверка корней
o=0
p=0
for i in range(len(rd1)):
	if (rd1[i]>0):
		print('неустойчива')
		break
	elif(rd1[i]<0):
		o+=1
	elif (rd1[i]==0):
		p+=1
	if ((o+p)==len(rd)):
		if (p!=0):
			print('на границе')
		else:
			print('устойчива')

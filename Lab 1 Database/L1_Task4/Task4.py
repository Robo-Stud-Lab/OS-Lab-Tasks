from math import factorial, exp
import sys

choice = [["Андрей", "Маша", "Таня", "Удар Молнии", 12, 100, "Андрей"],
       ["Никита","Серёжа", "Настя", "Оползень", 14, 200, "Никита"],
       ["Соня", "Максим", "Саша", "Ужасная прокрастинация", 8, 300, "Соня"],
       ["Катя", "Таня", "Костя", "Ураган", 17, 400, "Катя"],
       ["Даша", "Игорь", "Кирилл", "Цунами", 24, 300, "Даша"],
       ["Полина", "Леша", "Света", "Падение метеорита", 15, 200, "Полина"],
       ["Нина", "Ира", "Хуэйминь", "Создание нейросети", 3, 100, "Нина"],
       ["Ба Хю", "Ифань", "Не Ли", "Потоп", 19, 200, "Ифань"],
       ["Карлос", "Родригес", "Сантьяго", "Депортация", 30, 300, "Карлос"],
       ["Галя", "Арина", "Коля", "Скука", 3, 400, "Галя"]]


def GetChoice(n = ''):
	### Absorbs input and checks it

	while True:
		if n == '':
			n =	input("Введите предпочитаемый вариант от 1 до "+str(len(choice))+": ")

		try:
			n = int(n)
			if n > 0 and n <= len(choice): return n-1
			
		except: print("Пожалуйста, введите число\n")
			

def GetDays(n = ''):
	### Absorbs input and checks it

	while True:
		if n == '':
			n = input("Введите количество дней: ")

		try:
			n = int(n)
			if n > 0: return n

		except: print("Пожалуйста, введите число\n")


if len(sys.argv) > 2:
	X = GetChoice(sys.argv[1])
	N = GetDays(sys.argv[2])

elif len(sys.argv) == 2:
	X = GetChoice(sys.argv[1])
	N = GetDays()
else:
	X = GetChoice()
	N = GetDays()

case = choice[X]


per1 = float(case[5])/3 

m = N*case[5]/case[4]

m = int(m)
try:
	probability = per1**m*exp(-per1)/factorial(m)

	print('Шанс, что за '+str(N)+' дней случится '+case[3].lower()+' только со студентом '+case[6]+' равен: '+str(round(probability*100, 3))+'%')
except OverflowError:
	print('Well, it\'s too big to Python it, Sorry\n Try less days next time')
	



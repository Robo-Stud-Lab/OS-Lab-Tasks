print('Вводите числа через запятую:')
numbers = input().split(',')
natural, integer, coomplex, even, odd, prime, vesh = [], [], [], [], [], [], []
is_complex = True 
tempComplex = complex(1)

def is_prime(n):
	'''
	Checks wether given number is prime 
	'''
	if n < 2: return False
	if n % 2 == 0 : return n == 2
	if n % 3 == 0 : return n == 3
	
	i = 5; s = 2

	while i * i <= n:
		if n % i == 0: return False
		i += s
		s = 6 - s

	return True

for element in numbers:
	try: complex(element)	#For some reason this syntax depicts complex numbers
	except: is_complex = False

	if is_complex:
		tempComplex = complex(element)

		if tempComplex.imag != 0: coomplex.append(tempComplex)
		else: 
			element = float(element)
			if float.is_integer(element):
				integer.append(int(element))

				if element > 0: natural.append(int(element))
				if element != 0 and element % 2 == 0: even.append(int(element))
				elif element !=0: odd.append(int(element))

				if is_prime(element): prime.append(int(element))

			else: vesh.append(float(element))
	
	is_complex=True


def JoinNums(array):
	'''
	Turn every array element into a string, then joins them into a string
	'''
	for i in range(0, len(array)):
		array[i] = str(array[i])

	return ", ".join(array)

print('\nНатуральные числа: '+JoinNums(natural))
print('Целые числа: '+JoinNums(integer))
print('Явно-комплексные числа: '+JoinNums(coomplex))
print('Чётные числа: '+JoinNums(even))
print('Нечётные числа: '+JoinNums(odd))
print('Простые числа: '+JoinNums(prime))
vesh = vesh + integer
print('Вещественные числа: '+JoinNums(vesh))
print('Рациональные числа: '+JoinNums(vesh))

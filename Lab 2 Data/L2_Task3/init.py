import maths
import numpy as np
from Table import *

Data = Table(1,300)

MatExp = maths.MatExpectation(Data.matrix)
Variance = maths.Variance(Data.matrix,MatExp)

print('\n\nМатематическое ожидание заданной матрицы: ')
print(MatExp)
print('\n')
print('\n\nДисперсия заданной матрицы: ')
print(Variance)
print('\n')


ans = maths.check_correlation(Data.matrix, Data.N)

print("Лин.зависимость")
print(np.dstack(np.where(abs(ans[0]) > 0.7)))
print("Эксп.зависимость")
print(np.dstack(np.where(abs(ans[1]) > 0.7)))



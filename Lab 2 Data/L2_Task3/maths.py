import numpy as np
import math
## I AM AFRAID WE HAVE TO USE MATHS

def MatExpectation(arr):
    
    MatExpectation = []
    SumMat = 0

    for i in range(0, len(arr)):
        unique, counts = np.unique(arr[i], return_counts = True)

        for j in range(0, len(unique)):	
            SumMat += unique[j]*counts[j]/len(arr[i])

        MatExpectation.append(round(SumMat,2))
        SumMat = 0

    return MatExpectation


def Variance(arr,MatExp):
    Variance = []
    ard = np.copy(arr)
    MatExpSq = MatExpectation(ard**2)
    
    for i in range(0, len(MatExp)):
    	Variance.append(round(MatExpSq[i]-(MatExp[i])**2,2))
    
    return Variance


def lin_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    cov = 0
    s_x = 0
    s_y = 0
    for i in range(x.shape[0]):
        cov += (x[i] - x_mean)*(y[i] - y_mean)
        s_x += (x[i] - x_mean)**2
        s_y += (y[i] - y_mean)**2
    r = cov/math.sqrt(s_x*s_y)
    return r


def exp_correlation(x, y):
    print('\n\n\n')
    print(y)
    return lin_correlation(x, np.log(y))


def check_correlation(data, n):
    lin_corr_matrix = np.zeros((n, n))
    exp_corr_matrix = np.zeros((n, n))


    for i in range(n):
        for j in range(n):
            lin_corr_matrix[i][j] = lin_correlation(data[:, i], data[:, j])
            exp_corr_matrix[i][j] = exp_correlation(data[:, i], data[:, j])

    return lin_corr_matrix, exp_corr_matrix



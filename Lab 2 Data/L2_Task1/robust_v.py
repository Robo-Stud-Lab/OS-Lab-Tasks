import numpy as np
X = np.array([[3,6,2],[4,8,5],[3,9,2]],int)

miss = np.array([2,34,9]

X_vin = np.copy(X)

for i in np.arange(X.shape[0]):
	for j in np.arange(X.shape[1]):
		if [i,j] in miss:
			if [i, j-1] not in miss and (j-1) >= 0:
				X_vin[i, j] = X[i, j-1]
			else:
				if [i, j+1] not in miss and (j+1) <= 19:
					X_vin[i, j] = -999
		else:
			X_vin[i,j] = X[i,j]
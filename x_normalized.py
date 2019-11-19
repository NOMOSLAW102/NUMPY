import numpy as np
X= np.random.random((5,5))

x= X.mean()
U= np.subtract(X,x)
D= np.std(U)
Z= np.divide(U,D)
print (Z)
np.save('X_normalized', Z)
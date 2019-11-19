import numpy as np
a = np.linspace(1,100,100)
b = (a.reshape(10,10))
c = b**2
final = c[c%3==0]
print (final)
np.save('div_by_3.npy', final)

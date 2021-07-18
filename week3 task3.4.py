import numpy as np

array4 = np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

odds = (array4%2 ==1)

array4[odds] = -1

print (array4)






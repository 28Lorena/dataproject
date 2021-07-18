import numpy as np

arrayA = np.arange (1,5).reshape(2,2)
arrayB = np.arange (6,10).reshape(2,2)
arrayC = np.dot (arrayA, arrayB)

arrayE = np.sum (arrayC, axis = 0)
                    
print (arrayE)




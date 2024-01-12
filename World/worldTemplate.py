import numpy as np

def generateTemplate(size: int)->list:
    map = np.zeros(size**2)
    map.shape = (size,size)
    print(np.matrix(map))
    return map
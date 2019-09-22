import numpy as np

#solução de sistema de equações lineares
#3x - y + z = 1
#-2x + 3y - 3z = -19
#-x -3y - 4z = -15

a = np.matrix ([
        [3, -1, 1],
        [-2, 3, -3],
        [-1, -3, -4]
        ])

b = np.matrix ([
        [1],
        [-19],
        [-15]
        ])


aIn = np.linalg.inv(a)

print("solução:\n", aIn * b)
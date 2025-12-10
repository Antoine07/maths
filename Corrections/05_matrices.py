A = np.array([ [2,3], [4,1] ])
B = np.array([ [1,2], [2,5] ])

# Multiplier deux matrices
A@B

# Inverser une matrice ATTENTION AU ZERO INFORMATIQUE
A = np.array([[3,2], [1, -1] ])

InvA = np.linalg.inv(A)

# SOLUTION
InvA @ np.array([7,1])

# Système 3x3

A = np.array([[1, 1, 1 ], [2, -1, 3], [-1, 4, 1]])
b = np.array([6, 14, 2])

s = np.linalg.solve(A, b)
print(s)

x, y, z = s

# On vérifie que le système est solutionné par les valeurs trouvées par Numpy

print( x + y + z )
print( 2*x - y +3*z )
print( -x + 4*y + z )

# Solution 
A @ np.linalg.solve(A, b)
import numpy as np
mat = np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(mat)
U,S,VT = np.linalg.svd(mat)
print("U",U)
print("vt",VT)
print("s",np.diag(S))
reconstructed_matrix = np.dot(U,np.dot(np.diag(S),VT))
print("reconstructed_matrix",reconstructed_matrix)
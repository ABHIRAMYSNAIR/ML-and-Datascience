import numpy as np
def matrix(matrix_name,row,col):
    mat1=[]

    for i in range(0,r):
        mat2=[]
        for j in range(0,c):
          n=int(input(f"enter the elments of {matrix_name} row{i+1} and column{j+1}"))
          mat2.append(n)
        mat1.append(mat2)
    return mat1


r = int(input("enter the number of rows"))
c = int(input("enter the number of columns"))
matrix1=matrix("matrix1",r,c)
matrix2=matrix("matrix2",r,c)
print("matrix1",matrix1)
print("matrix2",matrix2)

print("add",np.add(matrix2,matrix1))
print("sub",np.subtract(matrix2,matrix1))
print("transpose",np.transpose(matrix1))
print("sqrt",np.sqrt(matrix1))
print("mul",np.multiply(matrix1,matrix2))

import numpy as np
arr1=np.array([1,2,3],ndmin=3)
print(arr1,"\n")
print(arr1.shape)
arr2=np.array([9,8,5])
print("array1 = ",arr1)
print("array2 = ",arr2)
print("result = ",arr1*arr2)
print(np.add(arr1,arr2))
print(arr1[-2:-1])
s=2
print(arr1*s)
print(np.__version__)
print(arr2[2])
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3)
print(newarr)
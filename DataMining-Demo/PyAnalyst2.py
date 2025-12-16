import numpy as np
arr = np.array([[5,8],
                [1,10],
                [31,67]])
# print(arr.reshape(3,2,-1))
for i, x in np.ndenumerate(arr):
    print(i, x)
# x = arr.copy()
# x = arr.view()
# x[1,0:] = [75,55]
# print(x)
# arr = np.array([[5,8],
#                 [1,10],
#                 [31,67]], dtype='f')
# print(arr[2] +arr[0])
# print(arr[0,1])
# print(arr[1,0:2])
# print(arr)
# print(arr.shape)
# print(x.base)
# print(arr.dtype)
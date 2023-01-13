import numpy as np
import matplotlib.pyplot as plt
a = [1,2,3,4,5]
print(a)

# numpy is a library for numerical computational 
import numpy as np
arr = np.array([1,2,4] 
)
print(arr, type(arr))
print("shape of the array: ",arr.shape)
print(len(arr))
print(arr[0],arr[1],arr[2])


arr2D = np.array([
    [2,3],
    [5,6],
    [8,9]]
)
print(arr2D, arr2D.shape, len(arr2D))
print(arr2D[0,1])
print(
    arr2D[0,0]*arr2D[0,1]
)
arr2D[0,0] = 7
print(arr2D)


# printing the 3d elements
# arr3D = np.array([
#     [
#         [1,2,3],
#         [2,3,6],
#         [4,9,5]
#     ],
#     [
#         [9,4,1],
#         [2,8,5],
#         [1,8,9]
#     ],
#     [
#         [2,6,9],
#         [6,8,2],
#         [2,7,1]
#     ]]
# )
# print(arr3D)
# print(arr3D[1,1,1])


arr2D[0] = [4,5]
print(arr2D)

zeros =np.zeros((4,5))
print(zeros)

ones = np.ones((3,))
print(ones)


consts = np.full((3,3),9)
print(consts)

rand = np.random.random((4,4))
print(rand)
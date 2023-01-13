import numpy as np

# arr = np.array([
#     [5,4,3,1],
#     [9,4,2,1],
#     [6,8,3,1]
# ])
# print(arr[:2,1:3])

# # extract last row and  col0 and col 1
# print((arr[-1,:2]))
# # extarct col 1 and col2 
# print(arr[:, 1:3])
# #extract third col
# print(arr[:, 2:3])
# # extract 2nd Row 
# print(arr[:, :3])

# # true where condition match otherwise false
# print(arr)
# bool_idx = [arr>=3]
# print(bool_idx)
# # print the elements in the array which is greater than 3 
# print(arr[arr>3])

# x= np.array([
#      [2,4],
#      [5,3]
# ])

# y= np.array([
#     [6,9],
#     [6,2]
# ])

#normally
# print(x,y)
# print(x + y)
# # using numpy calculation
# print(np.add(x,y))
# print(np.subtract(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))
# print(np.sqrt(x))


x= np.array([
     [2,4],
     [5,3]
])
print(x)
y= np.array([
    [6,9],
    [6,2]
])
print(y)

v = np.array([4,5])
w = np.array([3,6])

print(v.dot(w))
print(np.dot(v,w))

# matrix vector product; both  produce the same
print(x.dot(w))
print(np.dot(x,w))

print(x.dot(y))
print(np.dot(x,y))

#matrix transposition
print(x)
print(x.T)

u = np.array([
    [3,0,5],
    [6,7,3],
    [6,8,4]
])

print(u)
print(u.T)


print("sum of all elements of u: ", np.sum(u))

#sum of each column
print("sem of each column: ", np.sum(u, axis=0))
print("sum of all rows: ", np.sum(u, axis=1))


x=np.array([
    [3,4,5],
    [2,6,3],
    [8,4,1]
])

v=np.array([1,0,1])
# # for loop route approach
# y=np.empty_like(x)
# print(y)

# for i in range(len(x)):
#     y[i, :] = x[i, :] + v
# print(x)
# print(y)


# mathematical approach
stacked_v = np.tile(v, (3,1))
print(stacked_v)

print(x + stacked_v)
print(x+v)



x= np.array([1,2,3])
print(np.reshape(x, (3,1)))

x= np.array([
    [3,4,5],
    [6,2,1]
])

print(np.reshape(x, (3,2)))

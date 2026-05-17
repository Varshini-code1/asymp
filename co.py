# 1. Create an array from a Python list
ar = np.array([1, 2, 3, 4, 5])
print(ar)


# 2. Create an array of zeros
ar = np.zeros((2, 3))   # 2x3 array filled with 0.0
print(ar)


# 3. Create an array of ones
ar = np.ones((3, 2))    # 3x2 array filled with 1.0
print(ar)


# 4. Create an array filled with a specific value
ar = np.full((2, 2), 7)   # 2x2 array filled with 7
print(ar)


# 5. Create an identity matrix
ar = np.eye(4)   # 4x4 identity matrix
'''
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''
print(ar)
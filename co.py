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
# 6. Create an array with a range of values
ar = np.arange(0, 10, 2)   # Values from 0 to 8 with step 2
print(ar)

# 7. Create an array with evenly spaced values
ar = np.linspace(0, 1, 5)   # 5 values from 0 to 1 , d=(1-0)/(5-1)=1/4=0.25-> 0, 0.25, 0.5,0.75,1.
print(ar)


# 8. Create an empty array (uninitialized values)

ar = np.empty(2)   # May contain arbitrary values

print(ar)


#arrange the elements in ascending order

print(np.sort(ar))
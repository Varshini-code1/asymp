# nth bit in a number is set bit or not

def f1(num, n):  # Example: 100110, n = 3
    # Perform AND with shifted 1 to check nth bit
    # Example: 100110 & 000100
    if num & (1 << (n - 1)):
        print("\nSet")       # if result is non-zero → bit is 1
    else:
        print("\nNot Set")   # if result is zero → bit is 0

# taking input
x = int(input("Enter a number : "))
n = int(input("Enter bit number to check : "))

# function call
f1(x, n)

# set bit = 1
# example: n = 3
# 1001101 & 00000100

# counting part (as given)
c = 1
while n & 1 == 1:
    n = n >> 1   # shift right
    c = c + 1    # increment counter
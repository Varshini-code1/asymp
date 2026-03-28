def f1(n):
    ones = 0
    zeros = 0
    while(n):
        if n & 1 == 1:
            ones += 1
        else:
            zeros += 1
        n = n >> 1
    print("Ones :", ones, "Zeros", zeros)

num = int(input("Enter a number : "))
f1(num)
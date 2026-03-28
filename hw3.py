def f1(n):
    pos = 1
    while n & 1 == 0:
        n = n >> 1
        pos += 1
    print(pos)

num = int(input("Enter a number : "))
f1(num)
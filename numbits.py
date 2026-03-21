n = int(input("Enter n: "))
c = 0
while n:
    c += 1
    n >>= 1
print(c)
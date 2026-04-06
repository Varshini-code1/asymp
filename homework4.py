n = int(input())

while n > 1 and n % 8 == 0:
    n //= 8

if n == 1:
    print("Yes")
else:
    print("No")
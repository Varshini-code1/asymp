def armstrong(n):
    m = n
    sum = 0
    while n != 0:
        r = n % 10
        sum = sum + r * r * r
        n = n // 10
    if sum == m:
        return True
    else:
        return False

x = int(input("Enter your number : "))
if armstrong(x):
    print(x, "is armstrong number")
else:
    print(x, "is not an armstrong number")
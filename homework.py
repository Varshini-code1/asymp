def f1(n):
    result = 0
    while n > 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

num = 13
reversed_num = f1(num)

print("Original:", bin(num))
print("Reversed:", bin(reversed_num))
print("Reversed as number:", reversed_num)
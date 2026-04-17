def paren(s, l, r, p, n):
    # If full length reached, print
    if p == 2 * n:
        for x in s:
            print(x, end='')
        print("\n")
        return

    # Add ')' if valid
    if l > r:
        s[p] = "}"
        paren(s, l, r + 1, p + 1, n)

    # Add '{' if limit not reached
    if l < n:
        s[p] = "{"
        paren(s, l + 1, r, p + 1, n)


n = int(input("Enter number of parenthesis: "))
s = [""] * 2 * n
print("\n")
paren(s, 0, 0, 0, n)
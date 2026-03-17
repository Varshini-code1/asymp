a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

for n in range(a,b+1):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n,'is prime number')
    else:
        print(n,'is not a prime number')
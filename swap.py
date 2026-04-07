a=int(input("Enter a : "))
b=int(input("Enter b : "))
print("The numbers before swapping : a=",a,"b=",b)
a,b=b,a
print("The numbers after swapping : a=",a,"b=",b)

def swap1(a,b):
    print("Before Swapping : ",a,b)
    a=a+b
    b=a-b
    a=a-b
    print("After Swapping : ",a,b)

def swap2(a,b):
    print("Before Swapping : ",a,b)
    a=a^b
    b=a^b
    a=a^b
    print("After Swapping : ",a,b)

def swap3(a,b):
    print("Before Swapping : ",a,b)
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("After Swapping : ",a,b)

swap1(30,40)
swap2(30,40)
swap3(30,40)
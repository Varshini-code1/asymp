# Program to print number decreasing then increasing order

def incdec(n, num): #n=5,4,3,2,1,      num=5
    # Base case to return value when we reach our limit
    if(n<1 or n>num):
        return
    # Print decreasing first
    print(n) #5,4
    incdec(n-1,num)
    # Print increasing order
    print(n)

n = int(input("Enter any number n : ")) #5
incdec(n,n)
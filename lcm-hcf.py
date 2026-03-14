#HCF
n1=int(input("Enter big number : "))#28
n2=int(input("Enter small number : "))#16
a=n1#28
b=n2#16

while n2!=0:
    n3=n2 #n3=16, 12,4
    n2=n1%n2 #n2=12, 16/12= 4, 12/4=0
    n1=n3 #n1=16, 12, 4

HCF=n1
print("HCF = ",HCF)
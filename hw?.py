n=int(input("Enter number : "))
count=0
max_count=0

while n>0:
    if n&1:
        count+=1
        if count>max_count:
            max_count=count
    else:
        count=0
    n=n>>1

print(max_count)
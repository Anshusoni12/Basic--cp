n = int(input("Enter a no"))
sum =0
while(n>0):
    a=n%10
    n = n//10
    sum=sum+a
print("Sum:",sum)
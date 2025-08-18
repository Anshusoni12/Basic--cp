n=int(input("Enter a no:"))
temp=n
p=0
while(n>0):
   p=p*10+(n%10)
   n=n//10
if(temp==p):
   print("YES")
else:
   print("NO")

    
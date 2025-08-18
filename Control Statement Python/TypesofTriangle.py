a = int(input("Enter a first angle"))
b = int(input("Enter a Second angle"))
c = int(input("Enter a Third anlge"))
if((a+b+c==180)):
    if(a==90 or b==90 or c==90):
        print("It is Right Triangle")
    elif(a>90 or b>90 or c>90):
        print("It is Obtuse Triangle")
    else:
       print("It is a Acute Triangle")
else:
    print("Triangle is not valid")
   
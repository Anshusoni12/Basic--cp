T=int (input())
for i in range(T):
    S=input()
    vow=0
    cons=0
    for j in S:
        if j in "aeiouAEIOU":
            vow+=1
        else:
            cons+=1
    print(vow,cons)




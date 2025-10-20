from collections import Counter
t=int(input())
for _ in range (t):
    k,q=list(map(int,input().split()))
    a=list(map(int,input().split()))
    qn=list(map(int,input().split()))
    mine=min(a)
    res=""
    for i in qn:
        if i<mine:
            res=res+str(i)+ " "
        elif i>=mine:
            res=res+str(mine-1)+ " "
    print(res[:len(res)-1])


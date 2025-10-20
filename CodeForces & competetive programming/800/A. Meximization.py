from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    last=Counter(a)
    l1=[]
    l2=[]
    for k,v in last.items():
        if v==1:
            l1.append(k)
        else:
            l1.append(k)
            l2.extend([k]*(v-1))
    print(" ".join(map(str,l1+l2)))

    
            
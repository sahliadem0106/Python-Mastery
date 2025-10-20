from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    if (len(d.keys())<=2 and max(d.values())<=min(d.values())+1) or len(d.keys())==1:
        print("Yes")
    else:
        print("No")

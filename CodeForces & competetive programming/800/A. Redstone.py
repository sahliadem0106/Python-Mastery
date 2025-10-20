t=int(input())
o=0
iter=0
while o!=t:
    o+=1
    n=int(input())
    teeth=list(map(int,input().split()))
    from collections import Counter
    occ=Counter(teeth)
    ans=max(list(occ.values()))
    if ans >=2:
        print("yes")
    else:
        print("no")

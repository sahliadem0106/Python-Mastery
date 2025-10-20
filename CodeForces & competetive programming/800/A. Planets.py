from collections import Counter
t=int(input())
for _ in range(t):
    n,c=list(map(int,input().split()))
    a=list(map(int, input().split()))
    orbits=Counter(a)
    case1=len(orbits.keys())*c
    s=0
    s1=n
    s2=len(orbits.keys())*c
    for k,v in orbits.items():
        s += min(v, c)
    print(min(s1,s2,s))

from collections import Counter
t=int(input())
for _ in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a) or a[0]==1:
        print("YES")
    else:
        print("NO")
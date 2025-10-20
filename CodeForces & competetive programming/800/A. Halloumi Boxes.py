t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if k>1  or (set(l)=={l[0]}) or len(l)==1 or l==sorted(l):
        print("YES")
    elif k==1 and l!=sorted(l):
        print("NO")


n,x=map(int,input().split())
l=list(map(int,input().split()))
seen={}
for i in range(n):
    nek=x-l[i]
    if nek in seen:
        print()
    

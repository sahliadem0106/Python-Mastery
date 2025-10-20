t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a=sorted(a)
    if len(a):
        m=a[0]
    else:
        m=0
    for i in range(len(a)-1):
        if (a[i+1]-a[i])>m:
            m=a[i+1]-a[i]
    m1=(x-a[-1])*2
    print(m1) if m1>m else print (m)
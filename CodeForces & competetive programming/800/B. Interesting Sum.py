t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    maxi1=max(a)
    mini1=min(a)
    in1 = a.index(maxi1)
    in2 = a.index(mini1)
    if in1 > in2:
        a.pop(in1)
        a.pop(in2)
    else:
        a.pop(in2)
        a.pop(in1)
    maxi2=max(a)
    mini2=min(a)
    print(maxi2-mini2+maxi1-mini1)




t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    maxi1=max(a)
    mini1=min(a)
    a.pop(a.index(maxi1))                   #this is better
    a.pop(a.index(mini1))
    maxi2=max(a)
    mini2=min(a)
    print(maxi2-mini2+maxi1-mini1)
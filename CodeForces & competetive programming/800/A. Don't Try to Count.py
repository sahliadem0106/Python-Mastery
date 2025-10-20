t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=input()
    s=input()
    r=1
    c=0
    f=s in x
    if f==True:
        print(0)
    else :
        while c<5 and f==False:
            x+=x
            c+=1
            f=s in x
        print(c) if f==True else print(-1)
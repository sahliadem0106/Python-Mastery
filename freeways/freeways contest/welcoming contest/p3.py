n,k=map(int,input().split())
o=(n+1)//2
if k<=o:
    print(2*k-1)
else:
    print(2*(k-o))

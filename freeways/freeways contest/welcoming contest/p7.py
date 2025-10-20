n,k=map(int,input().split())
while k!=0:
    if str(n)[-1]=="0":
        n=n//10
    else:
        n=n-1
    k=k-1
print(n)
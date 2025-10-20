t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    listres=[]
    for i in range(n):
        if i<n-1 and f[i]>s[i+1]:
            s[i+1]=f[i]
        listres.append(f[i]-s[i])   
    ans = " ".join(map(str,listres))
    print(ans)

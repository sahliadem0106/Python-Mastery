n,x=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            ch=""
            if l[i]+l[j]==x and ch.find(str(i))==-1:
                ch=str(i)+str(j)
                print(str(i+1)+" "+str(j+1))

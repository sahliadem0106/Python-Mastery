from collections import Counter
n=int(input())
mat=[]
r=0
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
    if sum(row)>=2:
        r+=1
print(r)

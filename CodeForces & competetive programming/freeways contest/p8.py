n=int(input())
l=list(map(int,input().split()))
l=[abs(x) for x in l]
if min(l)==0:
    print("0")
else:
    print(min(l))
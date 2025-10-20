t=int(input())
for _ in range(t):
    n=int(input())
    i=1
    s=n+i
    while s%3==0:
        i+=1
        s=n+i
    i=0
    o=n-i
    while o%3==0:
        i+=1
        o=n-i
    m=min(o,s)
    if abs(n-m)>10 or abs(n-m)%2==0:
        print("First")
    else:
        print("Second")

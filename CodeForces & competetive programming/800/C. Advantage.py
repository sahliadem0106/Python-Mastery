'''t=int(input())
for _ in range(t):
    n=int(input())
    pi=list(map(int,input().split()))
    r=[]
    tbasem=max(pi)
    for into in pi:
        if into!=tbasem:
            r.append(into-tbasem)
        else:
            o=tbasem
            i=pi.index(tbasem)
            pi.pop(i)
            m=max(pi)
            pi.insert(i,o)
            r.append(o-m)
    print(' '.join(map(str, r)))
'''
t=int(input())
for _ in range(t):
    n=int(input())
    pi=list(map(int,input().split()))
    r=[]
    pi2=list(pi)
    pi2.sort(reverse=True)
    t1=pi2[0]
    t2=pi2[1]
    for i in pi:
        if i!=t1:
            r.append(i-t1)
        else:
            r.append(i-t2)
    print(' '.join(map(str, r)))
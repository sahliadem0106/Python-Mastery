import math
t=int(input())
for _ in range(t):
    n=int(input())
    b=input()
    s=()
    for i in range(n):
        if b[i]=="1":
            s.add(int(b[i])+1)
    for i in range(n):
        
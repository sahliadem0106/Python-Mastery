from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    ball=Counter(s)
    for i in ball.values():
        ans+=i
    ans+=len(ball)
    print(ans)

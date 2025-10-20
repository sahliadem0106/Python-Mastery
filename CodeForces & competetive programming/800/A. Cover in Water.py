t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    longest = max(len(part) for part in s.split('#'))
    if longest>=3:
        print("2")
    else:
        print(s.count('.'))
        
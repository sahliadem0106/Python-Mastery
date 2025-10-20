n=int(input())
words = []
for _ in range(n):
    words.append(input())
for i in range(n):
    if len(words[i])>10:
        print(words[i][0]+str(len(words[i])-2)+words[i][-1])
    else:
        print(words[i])
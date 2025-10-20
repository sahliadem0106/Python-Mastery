matrix = []
for _ in range(5):
    row = list(map(int, input().split()))  
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            x1=i
            x2=j
            break
print(str(abs(x1-2)+abs(x2-2)))
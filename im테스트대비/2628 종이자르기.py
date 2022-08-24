m, n = map(int, input().split())  # n: 가로 , m: 세로
#paper = [[1] * m for _ in range(n)]

T = int(input())
row = [0, n]
col = [0, m]
for t in range(T):
    case, num = map(int, input().split())
    #0 가로 , 1 세로
    if case == 0:
        row.append(num)
    else:
        col.append(num)

#정렬(이따 좌표 생각을 편하게 하기 위해서)
for i in range(len(row)-1):
    min_idx = i
    for j in range(i+1, len(row)):
        if row[j] < row[min_idx]:
            min_idx = j
    row[i], row[min_idx] = row[min_idx], row[i]

for i in range(len(col)-1):
    min_idx = i
    for j in range(i+1, len(col)):
        if col[j] < col[min_idx]:
            min_idx = j
    col[i], col[min_idx] = col[min_idx], col[i]

# 각 종이 조각의 넓이 계산
# 좌표처럼 생각하기
maxV = 0
for i in range(len(row)-1):
    for j in range(len(col)-1):
        val = 0
        for r in range(row[i], row[i+1]):
            for c in range(col[j], col[j+1]):
               val += 1
        if val > maxV:
            maxV = val

print(maxV)
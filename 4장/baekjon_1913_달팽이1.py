n = int(input())

#얕은 복사로 문제 해결법 list comprehension
dalpangE = [[0 for _ in range(n)] for _ in range(n)]

number = n*n
#초기값 세팅 1 (세로로 값 나열)
for i in range(n):
    dalpangE[i][0] = check
    check -= 1

#초기값 세팅 2
r, c = n-1, 0

#방향 생각: 동 북 서 남
dr = [0, -1, 0, 1] 
dc = [1, 0, -1, 0]

# 5*5 배열 기준으로 44 33 22 11 식으로 반복(방향 좌표값을..)
for i in range(n-1, 0, -1):
    for j in range(n):
        for k in range(4): #방향
            for d in range(1, i+1) #44 33 22 11 식으로
                nr = r + dr[k]*d
                nc = c + dc[k]*d
                dalpangE[nr][nc] = number                
                number -= 1

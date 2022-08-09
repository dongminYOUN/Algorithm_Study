N = int(input())
value = int(input())

#얕은 복사로 문제 해결법 list comprehension
dalpangE = [[0 for _ in range(N)] for _ in range(N)]

#초기값 세팅
number = N*N # 값
r, c = 0, 0  # 배열 인덱스
d = 0        # 회전 계수 

#방향 생각: 남 동 북 서 
dr = [1, 0, -1, 0] 
dc = [0, 1, 0, -1]

# 남 동 북 서 방향으로 회전 하는 함수
def turn(d):
    if d == 3:
        return 0
    return d + 1


#배열 채워넣기
while number > 0:  
    # 배열인덱스를 임시저장, 최종저장 여부는 마지막에 확인
    nr = r + dr[d]
    nc = c + dc[d]
    #이전에 저장한 값을 출력
    dalpangE[r][c] = number
    number -= 1
    #정해진 배열값을 벗어날 경우 회전
    if nr >= N or nr < 0 or nc >= N or nc < 0:
        d = turn(d)
        r, c = r + dr[d] , c + dc[d]
        continue
    #배열이 0이 아니라 채워져 있는 경우 회전
    elif dalpangE[nr][nc] != 0:
        d = turn(d)
        r, c = r + dr[d] , c + dc[d]
        continue
    #최종 저장
    r, c = nr, nc
    
# 원하는 값으로 출력
for i in dalpangE:
    for j in i:
        print(j, end=' ')
    print()

#입력한 값 배열 인덱스 찾기
for x in range(N):
    for y in range(N):
        if dalpangE[x][y] == value:
            print(x+1, y+1)

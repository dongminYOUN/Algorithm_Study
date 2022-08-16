N = int(input())

jirae = [input() for _ in range(N)]
user = [input() for _ in range(N)]

#지뢰 찾기 함수(테두리 값 탐색)
def find(r, c):
    # 북쪽부터 시계방향
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    cnt = d = 0

    for check in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        # 범위 안 체크, index에러 나지않게
        if 0 <= nr < N and 0 <= nc < N and jirae[nr][nc] == '*':
            cnt += 1
        d += 1

    return cnt

# 출력
# case 나눈 이유 for문 안에 한번에 하고싶었는데 되지않아서.. 유저가 지뢰 골랐을때와 안골랐을 때 차이 구분
case = 0
for r in range(N):
    for c in range(N):
        #지뢰 탐색
        if user[r][c] == 'x':
            if jirae[r][c] == '*':
                case = 1
                break

# 하나로 합치는 방법이 있을까?
for r in range(N):
    for c in range(N):
        # 1 유저가 지뢰 클릭한 경우
        # 지뢰 먼저 표시되어야 하니까 jirae 가장 먼저 출력
        if case == 1:
            if jirae[r][c] == '*':
                print('*', end='')
            elif user[r][c] == 'x':
                print(find(r, c), end='')
            else:
                print('.', end='')
            # 줄바꿈
            if c == N - 1:
                print()

        # 2 지뢰 클릭 없는 경우
        else:
            if user[r][c] == 'x':
                print(find(r, c), end='')
            else:
                print('.', end='')
            # 줄바꿈
            if c == N - 1:
                print()



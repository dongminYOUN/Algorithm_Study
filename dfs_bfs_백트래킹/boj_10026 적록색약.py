from collections import deque

def bfs(r,c, color, arr):             #일반
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    q = deque()
    q.append((r,c))                   #q. deque((r,c))이렇게 하니까 while문에서 바로 오류났음. r,c를 불러올 수 없었다.
    visited[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == color:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
# 입력
N = int(input())
n_arr = [list(input()) for _ in range(N)]       # 기본값
visited = [[0] * N for _ in range(N)]

RG_arr = [[0] * N for _ in range(N)]            # 적록색약용 배열
for r in range(N):
    for c in range(N):
        if n_arr[r][c] == 'G':
            RG_arr[r][c] = 'R'
        else:
            RG_arr[r][c] = n_arr[r][c]

normal = RG = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs(r,c, n_arr[r][c], n_arr)
            normal += 1

visited = [[0] * N for _ in range(N)]       # 방문처리 초기화
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            bfs(r,c, RG_arr[r][c], RG_arr)
            RG += 1

print(normal, RG)


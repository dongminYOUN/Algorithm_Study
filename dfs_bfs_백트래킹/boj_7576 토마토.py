from collections import deque

def bfs():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt = 0
    # q = deque()
    # for i in li:
    #     q.append(i)
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            tomato[r][c] = 1            # 토마토는 익었으니까
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    if tomato[nr][nc] == 0:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
        cnt += 1

    # 토마토 전체 익었는지 확인
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                return -1
    else:
        return cnt -1           # -1 한 이유 마지막에 q에 1개 남았을 때. 즉, 더이상 갈 곳을 저장 할 수 없는 상태에도 while문이 돌아가서 cnt +1 을 하기때문

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]* M for _ in range(N)]
q = deque()
#li = []
# 시작 좌표 찾기
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            #li.append([r,c])
            q.append((r,c))
            visited[r][c] = 1

print(bfs())



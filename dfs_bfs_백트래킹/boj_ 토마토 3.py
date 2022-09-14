from collections import deque


def bfs():
    dr = [-1, 0, 1, 0, 0, 0]
    dc = [0, 1, 0, -1, 0, 0]
    dh = [0, 0, 0, 0, -1, 1]
    cnt = 0
    # q = deque()
    # for i in li:
    #     q.append(i)
    while q:
        for i in range(len(q)):
            h, r, c = q.popleft()
            tomato[h][r][c] = 1  # 토마토는 익었으니까
            for d in range(6):
                nr = r + dr[d]
                nc = c + dc[d]
                nh = h + dh[d]
                if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and visited[nh][nr][nc] == 0:
                    if tomato[nh][nr][nc] == 0:
                        q.append((nh, nr, nc))
                        visited[nh][nr][nc] = 1
        cnt += 1

    # 토마토 전체 익었는지 확인
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[z][i][j] == 0:
                    return -1
    else:
        return cnt - 1


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque()
# li = []
# 시작 좌표 찾기
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 1:
                # li.append([r,c])
                q.append((h, r, c))
                visited[h][r][c] = 1

print(bfs())

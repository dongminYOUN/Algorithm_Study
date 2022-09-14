from collections import deque

# bfs 할때마다 경로를 다 구하고 list에 저장, 그 값중에 가장 큰 값 찾기.
# bfs 하나하고 visited 초기화 이런식으로 접근?  난 visited를 처리 안하면 최단거리를 탐색하는 방법을 모름..
# 다른 방법이 없을까??
# python은 시간초과... 그러나 pypy는 통과

def bfs(r,c):
    global visited
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    Q.append((r,c))
    visited[r][c] = 1
    cnt = 0
    while Q:
        for _ in range(len(Q)):
            r, c = Q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                    if gold[nr][nc] == 'L':
                        Q.append((nr,nc))
                        visited[nr][nc] = 1
        cnt += 1

    shortcut.append(cnt-1)          #-1인 이유 더이상 갈 곳이 없을때도 Q.pop을 하여 while문이 작동하니까

    visited = [[0] * M for _ in range(N)]    # bfs가 끝날때마다 방문처리 초기화
    # for i in range(N):
    #     for j in range(M):
    #         visited[i][j] = 0


N, M = map(int,input().split())
gold = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
shortcut = []
Q = deque()

for r in range(N):
    for c in range(M):
        if gold[r][c] == 'L':
            bfs(r,c)

print(max(shortcut))


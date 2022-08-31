def dfs(r,c):
    global cnt                          # 총 몇단지가 있는지 파악하기 위해서
    global danji
    # 상 부터 시계방향
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    stack = [(r,c)]
    home = 1                            # 단지수 파악(처음부터 스택에 값을 넣기에 + 1)
    while stack:
        r, c = stack.pop()
        visited[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if jido[nr][nc] == 1 and visited[nr][nc] == 0:
                    if (nr, nc) not in stack:   # 갈 곳이 중복되서 stack에 저장되는 경우가 있음 그렇기에 제외
                        stack.append((nr, nc))
                        home += 1
    cnt += 1
    danji.append(home)

N = int(input())
jido = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
danji = []
# visited = 0 이면서 jido = 1인 곳을 탐색
for r in range(N):
    for c in range(N):
        if jido[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)

ans = sorted(danji)
# 출력
print(cnt)
for i in ans:
    print(i)

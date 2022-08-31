def dfs(v):
    global cnt
    visited[v] = 1
    for w in G[v]:
        if visited[w] == 0:
            cnt += 1
            dfs(w)


V = int(input())
E = int(input())

G = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

#1번 컴퓨터를 통해 바이러스 걸린 수 몇개인지 파악
cnt = 0
dfs(1)
print(cnt)
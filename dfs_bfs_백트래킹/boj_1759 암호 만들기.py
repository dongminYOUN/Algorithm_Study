import sys
sys.setrecursionlimit(10**8)

def solve(depth, k, N, M):
    if depth == M:
        vowel = 0       # 모음
        jaum = 0        # 자음
        for j in ans:
            if j in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                jaum += 1
        # 모음 1개, 자음 2개 이상일 때 만 저장
        if vowel >= 1 and jaum >= 2:
            return print(''.join(ans))

    else:
        for i in range(k, N):
            if visited[i] == 0:
                visited[i] = 1
                ans.append(str_li[i])
                solve(depth+1, i+1, N, M)
                ans.pop()
                visited[i] = 0



M, N = map(int, input().split())
str_li = sorted(input().split())
ans = []
visited = [0] * N
solve(0, 0, N, M)
N = int(input())

jirae = [list(map(int, input().split())) for _ in range(N)]
user = [list(map(int, input().split())) for _ in range(N)]

for line in jirae:
    print(*line)



TC = int(input())

for tc in range(TC):
    N, M = map(int, (input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # M*M 배열부터 만들기 -> 순회시키기 1번 가로열부터 2번 세로열
            ans = 0
            for r in range(M):
                for c in range(M):
                    ans += arr[r+i][c+j]
            if ans > maxV:
                maxV = ans

    print(f'#{tc+1} {maxV}')



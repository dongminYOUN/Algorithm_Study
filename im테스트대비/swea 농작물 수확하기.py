TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = 0
    for i in range(N//2):
        for j in range(N//2 -i, N//2+1+i):
            ans += arr[i][j]       # 위에서부터 삼각형
            ans += arr[N-1-i][j]   # 아래서부터 삼각형

    for i in range(N):
        ans += arr[N//2][i]        # 가장 긴 가로줄 체크

    print(f'#{tc+1} {ans}')



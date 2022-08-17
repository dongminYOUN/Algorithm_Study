TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    #상 부터 시계방향 회전
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    maxV = 0

    for r in range(N):
        for c in range(N):
            temp = arr[r][c]            #초기값
            #십자가
            for d in range(0,7,2):      #방향 벡터 짝수
                for i in range(1,M):    # 1 ~ M-1
                    nr = r + dr[d] * i
                    nc = c + dc[d] * i

                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            if temp > maxV:
                maxV = temp


            #대각선
            temp = arr[r][c]
            for d in range(1,8,2):      # 방향 벡터 홀수
                for i in range(1,M):    # 1 ~ M-1
                    nr = r + dr[d] * i
                    nc = c + dc[d] * i

                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            if temp > maxV:
                maxV = temp

    print(f'#{tc+1} {maxV}')

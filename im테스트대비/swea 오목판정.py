TC = int(input())
for tc in range(TC):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # 상 부터 시계방향
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    ans = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    cnt = 1
                    #if 0 <= nr <N and 0 <= nc < N:
                    while 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 'o':
                            nr += dr[d]
                            nc += dc[d]
                            cnt += 1
                        else:
                            break

                        if cnt == 5:
                            ans += 1
                            break
    if ans >= 1:
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')




    # 스도쿠 처럼 생각해서 가로줄, 세로줄, 대각선 탐색
    # 가로줄
    # a1 = 0
    # for r in range(N):
    #     cnt = 0
    #     for c in range(N):
    #         if arr[r][c] == 'o':
    #             cnt += 1
    #             if cnt == 5:
    #                 a1 = 1
    #                 break
    #         else:
    #             cnt = 0
    #
    # # 세로줄
    # a2 = 0
    # for c in range(N):
    #     cnt = 0
    #     for r in range(N):
    #         if arr[r][c] == 'o':
    #             cnt += 1
    #             if cnt == 5:
    #                 a2 = 1
    #                 break
    #         else:
    #             cnt = 0
    #
    # # 대각선1 ////
    # a3 = 0
    # for r in range(N):
    #     for c in range(N):
    #         cnt = 0
    #         if r <= N-5 and c >= 4:
    #             for i in range(5):
    #                 if arr[r+i][c-i] == 'o':
    #                     cnt += 1
    #                 else:
    #                     cnt = 0
    #             if cnt == 5:
    #                 a3 = 1
    #                 break
    # # 대각선2 \\\\
    # a4 = 0
    # for r in range(N):
    #     for c in range(N):
    #         cnt = 0
    #         if r <= N-5 and c <= N-5:
    #             for i in range(5):
    #                 if arr[r+i][c+i] == 'o':
    #                     cnt += 1
    #                 else:
    #                     cnt = 0
    #             if cnt == 5:
    #                 a4 = 1
    #                 break
    #
    # if a1 + a2 + a3 + a4 >= 1:
    #     ans = 'YES'
    # else:
    #     ans = 'NO'
    #
    # print(f'#{tc+1} {ans}')




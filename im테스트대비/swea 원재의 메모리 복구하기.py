#import sys; sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    # 제일 왼쪽 부터 값을 넣어 원하는 값이 맞는지 체크
    memory = list(map(int, input()))
    N = len(memory)
    ans = [0] * N

    cnt = 0
    for i in range(N):
        if memory[i] == ans[i]:
            pass
        else:
            for j in range(i, N):
                ans[j] = memory[i]
            cnt += 1
            if ans == memory:
                break

    print(f'#{tc+1} {cnt}')

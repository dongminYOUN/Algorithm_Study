import sys; sys.stdin = open('ladder1.txt', 'r')

for tc in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        #초기값
        r, c = 0, x
        if ladder[r][c] == 0:
            continue
        while r < 99:
            #계속 내려가는 값
            r += 1

            #왼쪽
            if c > 0 and ladder[r][c-1] == 1:
                while c != 0 and ladder[r][c-1] != 0:
                    c -= 1
                # r = r + 1
            #오른쪽
            elif c < 99 and ladder[r][c+1] == 1:
                while c != 99 and ladder[r][c+1] != 0:
                    c += 1
               # r = r + 1

        if ladder[r][c] == 2:
            print(f'#{tc+1} {x}')
            break





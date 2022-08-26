TC = int(input())
for tc in range(TC):
    N = int(input())
    li = input().split()
    div1 = []
    div2 = []
    if N % 2 == 0:              # 짝수
        for i in range(N):
            if i < N//2:
                div1.append(li[i])
            else:
                div2.append(li[i])
    else:                       # 홀수
        for i in range(N):
            if i <= N//2:
                div1.append(li[i])
            else:
                div2.append(li[i])

    shuffle = []
    for i in range(N//2):
        shuffle.append(div1[i])
        shuffle.append(div2[i])
    if N % 2 == 1:
        shuffle.append(div1[N//2])

    print(f'#{tc+1}', end=" ")
    for i in shuffle:
        print(i, end=" ")
    print()






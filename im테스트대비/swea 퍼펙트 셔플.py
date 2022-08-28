TC = int(input())
for tc in range(TC):
    N = int(input())
    li = input().split()
    div1 = []
    div2 = []
    if N % 2 == 0:
        for i in range(N):
            if i < N//2:
                div1.append(li[i])
            else:
                div2.append(li[i])
    else:
        for i in range(N):
            if i <= N//2:
                div1.append(li[i])
            else:
                div2.append(li[i])

    shuffle = [] # a d / b e / c f
    for i in range(N//2):
        shuffle.append(div1[i])   # 1 2 3
        shuffle.append(div2[i])   # 4 5
    if N % 2 == 1:
        shuffle.append(div1[N//2])

    print(f'#{tc+1}', end=" ")
    for i in shuffle:
        print(i, end=" ")
    print()






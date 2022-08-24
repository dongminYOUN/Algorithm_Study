arr = [[0] * 101 for _ in range(101)]

for _ in range(4):
    # 직사각형 시작과 끝 좌표
    m1, n1, m2, n2 = map(int, input().split())

    for r in range(n1, n2):
        for c in range(m1, m2):
            # 겹치는 넓이 중복 제거하며 배열에 추가
            arr[r][c] = 1

ans = 0
for r in range(101):
    for c in range(101):
        if arr[r][c] == 1:
            ans += 1

# for i in arr:
#     for j in i:
#         print(j, end =' ')
#     print()

print(ans)
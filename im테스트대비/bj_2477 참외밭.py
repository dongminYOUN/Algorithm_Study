N = int(input())
info = [list(map(int, input().split())) for _ in range(6)]
#여기서 size만 따로 저장
size = []
for i in range(6):
    size.append(info[i][1])

idx = size.index(max(size))
row1 = size[idx]                    # 가장 큰 가로
# print(idx, size)

# idx: 가로, idx-1 = 첫번째 세로, idx+1 : 두번째 세로 / 회전 가능하게
# col1 : 가장 큰 세로 , col2 : 작은 세로
idx1, idx2 = (idx-1) % 6, (idx+1) % 6

# row1의 idx 기준으로 앞 뒤 값은 무조건 방향 전환임 즉 사각형 넓이를 유추할 수 있다는 뜻

if size[idx1] > size[idx2]:
    max_idx = idx1
    col1, col2 = size[max_idx], size[idx2]
elif size[idx1] < size[idx2]:
    max_idx = idx2
    col1, col2 = size[max_idx], size[idx1]
#print(col1, col2)

# 큰 세로 기준으로 가로 한번더 확인 / 둘중에 작은 값확인
idx3, idx4 = (max_idx -1) % 6, (max_idx + 1) % 6
if size[idx3] > size[idx4]:
    row2 = size[idx4]
else:
    row2 = size[idx3]
#print(row1, row2)

#넓이
result = row1 * col2 + row2 * (col1 - col2)
#참외수
print(result * N)





# 상하 좌우
# L : 왼쪽 한칸, R : 오른쪽 한칸.  U : 위 한칸, D : 아래 한칸
# y = 가로,  x= 세로

# 초기값 설정
x, y= 1, 1

N = int(input()) # 배열 크기
move_list = input().split()

#이동
for move in move_list:
    if move == "L":        
        y -= 1
    elif move == "R":
        y += 1
    elif move == "U":
        x -= 1
    elif move == "D":
        x += 1
    # 여기서 만약 범위를 벗어나게 된다면 했던 입력 그대로 반환
    if x > N:
        x -= 1
    elif x < 1:
        x += 1    
    elif y > N:
        y -= 1    
    elif y < 1:
        y += 1
             
print(x ,y)



# #이동'만' 생각하기 (값을 저장하지 않은 상태)

# for move in move_list:
#     if move == "L":        
#         ny = y - 1
#     elif move == "R":
#         ny = y + 1
#     elif move == "U":
#         nx = x - 1
#     elif move == "D":
#         nx = x + 1
#     print(nx, ny)

#     if nx < 1 or nx > N or ny < 1 or ny > N:
#         continue
#     # 이동한 좌표값을 저장해 주어야 하는데 continue를 통해 저장하지 않음.
#     x, y = nx, ny

# print(x, y)

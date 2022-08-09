N = int(input())
x, y = 1, 1

# dx, dy 로 인덱스 설정해서 움직이기
# L R U D 로 생각하기. 1,1  1,2 1,3

move_list = input().split()

move_type = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] 


for move in move_list:
    #이동'만' 생각하기 (값을 저장하지 않은 상태)
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 이동한 좌표값을 저장해 주어야 하는데 continue를 통해 저장하지 않음.
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue

   
    x, y = nx, ny
    
print(x, y)
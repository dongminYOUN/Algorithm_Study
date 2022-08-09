#왕실의 나이트
#초기 위치를 생각하기.
# 가로x = a,b,c ... 세로y = 1,2,3 ...

position = input()

x, y = ord(position[0]), int(position[1])
#print(x, y)

#움직일수 있는 경우의 수를 만들고 
# 이동을 8번해서 그 때 범위 밖이라면 count를 하지않는거지. move를 따로 저장
count = 0
move_list = [
    (2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)
]
for move in move_list:
    #이동했는지 여부만 확인
    nx = x + move[0]
    ny = y + move[1]
    
    #print(nx, ny)

    if ord('a') <= nx <= ord('h') and 1 <= ny <= 8:
        count += 1
    
print(count)
    



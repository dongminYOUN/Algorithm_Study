#게임 개발
'''
육지=0 바다=1
회전을 한다는 것이 그냥 그 좌표로 이동했다가 안되면 돌아간다 라고 생각 
그 방향을 유지한 채로 뒤로 가는거... 이때 값이 1이면 무조건 fail.
방향을 움직이면 그 포지션을 1로 바꾸는건 어떤가...
'''

#세로크기 N, 가로크기 M
N, M = map(int, input().split())

x, y, d = map(int, input().split())

#위치값 저장 ground_ocean = go
go_li = []
for i in range(N):
    go_li.append(list(map(int, input().split())))

#북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽 방향으로 회전 북 -> 서 -> 남 -> 동
def turn(d):
    if d == 0:
        return 3
    return d - 1

cnt = 1 # 처음 육지 밟은곳도 방문이라 생각
rot = 0 # 회전수 표시
while True:
    #왼쪽 회전부터 시작(문제조건)
    d = turn(d)
    #회전이 4가 된 경우(모든 방향이 바다인경우)
    if rot == 4:
        # 180도 회전해서 뒤로가야하니까
        d = turn(turn(d))
        if go_li[x + dx[d]][y + dy[d]] == 1:
            break
        elif go_li[x + dx[d]][y + dy[d]] == 2:
            x = x + dx[d]
            y = y + dy[d]
            # 다시 원래 바라보는 방향 전환
            d = turn(turn(d))
            rot == 0
            cnt += 1
            continue

    #<일반적인 경우 회전(0,1,2,3)>
    #바다(1) or 가본 곳(2)이면 회전
    if go_li[x + dx[d]][y + dy[d]]: #1, 2 다가능
        rot += 1
    #육지(0)이면 간 곳 표시(2)
    else:
        #위치하고 있는 값은 육지니까 -> 2로 간곳 표시
        go_li[x][y] = 2
        # 위치 변경
        x = x + dx[d]        
        y = y + dy[d]
        cnt += 1
        rot = 0

print(cnt)


#게임 개발
# 육지=0 바다=1
# 회전을 한다는 것이 그냥 그 좌표로 이동했다가 안되면 돌아간다 라고 생각 
# 그 방향을 유지한 채로 뒤로 가는거... 이때 값이 1이면 무조건 fail.
# 방향을 움직이면 그 포지션을 1로 바꾸는건 어떤가...

#세로크기 N, 가로크기 M
N, M = map(int, input().split())

x, y, direction = map(int, input().split())

#위치값 저장
ground_ocean = []
for i in range(N):
    ground_ocean.append(list(map(int, input().split())))
  
#print(ground_ocean)

#초기위치 설정
ground_ocean[x][y]

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]




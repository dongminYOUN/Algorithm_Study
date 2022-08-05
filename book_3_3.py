# 예제 3-3. 숫자 카드 게임

N, M = map(int, input().split())    # N:행, M:열
                                    # M의 역할이 없다. for문 내 입력시 M의 값보다 많이 들어가면 실행 안되게 해야할까?
min_list = []
for i in range(N):
    sub_list = list(map(int, input().split()))  
    min_list.append(min(sub_list))      # 입력 받은 list중 가장 작은 값

print(max(min_list)) #가장 작은 값들 중 제일 큰 값

# 그리디 방식으로 다시풀기.
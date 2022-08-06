#주유소

#전개방식 생각
#도시값이 최소면 무조건 남은 도로길이 곱하기
#최소값은 아니지만 도시의 리터값이 그 다음에 나올 값보다 작은경우..
#아니라면 도로길이 하나만 곱
#처음에 값을 저장하고... 그다음 리스트왔을때 그게 
#뭐가 더크냐? 생각하기

city = int(input())
road_list = list(map(int, input().split()))
liter_list = list(map(int, input().split()))


#가장 마지막 값 제거(마지막 도시의 리터는 의미가없다. 오히려 최소값에 영향을 미칠수 있음)
liter_list.remove(liter_list[-1])

cost = 0
first = liter_list[0]

for i in range(city-1):
    if liter_list[i] == min(liter_list):
        cost += liter_list[i] * sum(road_list[i:]) #시작인덱스 부터 끝까지 합(남은 도로길이의 합)
        break
    # 순간마다 최소값을 뽑아주는 것
    elif liter_list[i] < first:
        first = liter_list[i]

    cost += first * road_list[i]
    
print(cost)


#test case 도시 리터 가격
# 5 3 4 7 1 2 8 5           
    

idx=liter_list.index(min(liter_list))
cost=liter_list[idx] * sum(road_list[idx:])

for i in range(idx):
   
    if liter_list[i] < first:
        first = liter_list[i]
        
    cost += first * road_list[i]
    
print(cost)

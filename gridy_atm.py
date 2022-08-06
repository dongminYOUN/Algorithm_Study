# ATM
T = int(input())
people = list(map(int, input().split()))

people.sort()
wait_time = 0

#무조건 작은 수 부터 나열하면 된다.
for i in range(T):
    wait_time += sum(people[:(i+1)])    
    # 1 / 1+2/ 1+2+3/ 1+2+3+4 식으로 더하기위함 index활용
print(wait_time)
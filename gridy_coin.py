#coin
number, money = map(int, input().split())
coin_list =[]
for i in range(number):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)


count = 0

for coin in coin_list:
    #입력된 돈을 가장 큰 값의 동전으로 그때 쓰인 동전의 갯수를 알 수 있다.
    if money >= coin:       
        count += money // coin
        money = money % coin

#동전의 갯수        
print(count)
#예제 3-1 거스름돈
n = int(input())

#거스름돈 list
charge_list = [500, 100, 50, 10]
count = 0
charge_dict = {}

# 몇개의 거스름돈이 나왔는지 dictionary로 저장해볼까
# while문을 통해서 입력받은 값을 계속 감소시킴
while n != 0:    
    if n >= 500:
        n = n - charge_list[0]        
        count += 1
        #$charge_dict['500'] += 1 dictionary value값 증가 어떻게?
    elif n >= 100:
        n = n - charge_list[1]
        count += 1
    elif n >= 50:
        n = n - charge_list[2]
        count += 1
    else:
        n = n - charge_list[3]
        count += 1
     

print(count)
print(charge_dict)

#책 답안
# for coin in list:
#     count += n // coin
#     n %= coin

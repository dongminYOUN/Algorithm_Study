money = int(input())
stock_li = list(map(int, input().split()))

#1월 1일부터 1월 14일까지 고정 크기 14

money2 = money
#준현 BNP
BNP = 0
for stock in stock_li:
    if stock <= money:
        BNP += money // stock
        money = money % stock

BNP = stock_li[13] * BNP + money

#성민 TIMING / 3일 연속 하락(상승) 다음날 전량 매수(매도)
TIMING = buy = sell = 0 
for i in range(1, len(stock_li)):
    #사는 조건
    if stock_li[i] <= money2 and buy == 3:
        TIMING += money2 // stock_li[i]
        money2 = money2 % stock_li[i]        
        buy = 1
    #파는 조건
    if TIMING !=0 and sell == 3:
        money2 = stock_li[i] * TIMING
        sell = 1
        TIMING = 0
    
    if stock_li[i-1] > stock_li[i]: #하락
        buy += 1 
        sell = 1

    elif stock_li[i-1] < stock_li[i]: #상승
        buy = 1
        sell += 1
    
TIMING = stock_li[13] * TIMING + money2

#print(BNP, TIMING)

if TIMING > BNP:
    print("TIMING")
elif TIMING < BNP:
    print("BNP")
#시각
# 00시 00분 00초 ~ N시 59분 59초까지 
# 3이 하나라도 포함

n = int(input())
count = 0

# 시
for hour in range(n+1):
    #분
    for minute in range(60):
        #초
        for second in range(60):
            #합친 문자열 안에 3이 하나라도 들어가 있으면 count
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)
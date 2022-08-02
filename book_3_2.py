# 5 8 3 / 입력 5개, 8번 더하기, 연속되서 3번까지
# 2 4 5 4 6  답은 46

N, M, K = map(int, (input().split()))

T = list(map(int, input().split())) # 배열 N개 입력
T.sort(reverse=True)

s = 0

#최대값 2개가 같으면 무조건 번갈아가면서 쓰면 되기에 가장 큰 수 더하기 가능
if T[0] == T[1]:
    s = T[0] * M
else:
    #큰 while문 M번 더하기기능 / 값을 더할때 마다 M 감소
    while M != 0:
        count = 0
        #같은 인덱스를 연속해서 K번 반복하기 위함
        while True: 
            if count < K:
                s += T[0]
                M -= 1
                count += 1
                print(count)
            else:
                s += T[1]
                M -=1
                break
#while을 두개한 이유, 최대값 합 -> 2번째 최대값 1번 -> 다시 최대값 합 반복위해서.
print(s)
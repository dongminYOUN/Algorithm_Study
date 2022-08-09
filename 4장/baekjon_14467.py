#백준 소가 길을 건너간 이유 1
#왼쪽 0, 오른쪽 1

#처음에 입력받은 숫자는 그냥 저장.
#여기서 뒤에 입력받은 숫자 값이 바뀌면 count +1
# dictionary로 저장해서 key 값이 다르면 count

N = int(input())

cow_dict = {}
count = 0

for i in range(N):
    cow, position = input().split()
    #print(cow_dict)

    #딕셔너리로 만들어서 처음 넘버는 저장, 그 후 1, 0 값이 바뀌면 count
    for key, val in cow_dict.items():        
        if key == cow and val != position:
            count += 1
    cow_dict[cow] = position

print(count)



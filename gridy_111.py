#잃어버린 괄호

sentence = input().split('-')


# 마이너스 값을 최대로 해야 가장 작은 수를 만들 수 있다.
# 수식 3+2 - 1+5+3 - 4+5   
# 1. 마이너스가 한번만 나오면 그 뒤에 값을 다 합쳐서 빼면 됨.
# 2. 마이너스 묶음들을 더하고 마지막에 빼기
sum_list = []

print(sentence)

  
for divide in sentence:
    #마이너스 기준으로 구분된 숫자들을 합친다.
    print(divide.split('+'))
    sum_list.append(sum(map(int, divide.split('+'))))



print(sum_list[0] -sum(sum_list[1:]))
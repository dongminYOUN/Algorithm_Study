# 별 찍기 - 19
n = int(input())



# 별 테두리 / 기존값을 계속 누적하고싶은데.. 재귀함수?
# 배열 값을 바꿔준다고 생각해보자
def star(num):
    if 

    x = 4 * (n -1) + 1
    for i in range(x):    
        if i == 0 or i == x-1:
            print('*'*x)
        else:
            print('*', end="")
            print(' '*(x-2), end="")
            print('*')




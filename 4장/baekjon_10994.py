# 별 찍기 - 19
n = int(input())

x = 4 * (n -1) + 1

# 별 테두리 / 기존값을 계속 누적하고싶은데..
for i in range(x):    
    if i == 0 or i == x-1:
        print('*'*x)
    else:
        print('*', end="")
        print(' '*(x-2), end="")
        print('*')




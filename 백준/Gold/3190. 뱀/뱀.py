
#뱀 문제
import sys
from collections import deque
n = int(sys.stdin.readline()) # input 1
d = 0
direction = [(1,0),(0,1),(-1,0),(0,-1)] # L(왼쪽), D(오른쪽) , 서,남,동,북 #가로
snake = deque([[0,0]]) # 뱀 초기값.
fruit = []

a_c = int(sys.stdin.readline())
for i in range(a_c):
    x,y = map(int,sys.stdin.readline().split())
    fruit.append((y-1,x-1))
#print("fruit list : ",end = '')
#print(*fruit)

time = 0
is_game_over = False
o_c = int(sys.stdin.readline())
dir = direction[0]
time_dif = 0
for i in range(o_c): # 방향 o_c번 꺾기.
    change_time, c_d = map(str,sys.stdin.readline().split()) # 꺾을 시간과 어디로 꺾을건지 정함.
    time_dif = int(change_time) - time

    for j in range(time_dif):
        #이동하기전에, 먼저 앞이 벽인지, 자신과 부딪치는지 확인.
        time += 1
        head = snake[-1]
        pre_move = (head[0] + dir[0], head[1] + dir[1]) #앞의 위치

        if pre_move[0] >=n or pre_move[1] >=n or pre_move[0] < 0 or pre_move[1] < 0 or pre_move in snake: #is_game_over 만약에 앞이 벽일때,
            #print("out of graph" + str(pre_move))
            is_game_over = True
            break
        else:
            if pre_move in fruit:
                fruit.remove(pre_move)
                # print("rest_fruit")
                # print(fruit)
            else:
                snake.popleft()
            snake.append(pre_move)
        #print(snake)
    if(is_game_over):
        break
    # 방향전환
    if c_d in 'D':
        #print('change dir D')
        dir = direction[(d + 1) % 4]
        d = (d + 1) % 4

    else:
        #print('change dir L')
        dir = direction[(d + 3) % 4]
        d = (d + 3) % 4

while not is_game_over:

    time += 1
    head = snake[-1]
    pre_move = (head[0] + dir[0], head[1] + dir[1])  # 앞의 위치

    if pre_move[0] >= n or pre_move[1] >= n or pre_move[0] < 0 or pre_move[1] < 0 or pre_move in snake:  # is_game_over 만약에 앞이 벽일때,
        #print("out of graph" + str(pre_move))
        is_game_over = True
        break
    else :
        if pre_move in fruit:
            fruit.remove(pre_move)
            #print("rest_fruit : ", end = "")
            #print(fruit)
        else:
            snake.popleft()
        snake.append(pre_move)

    #print(snake)
print(time)
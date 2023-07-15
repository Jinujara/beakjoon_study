import sys
import itertools
n,m = map(int,sys.stdin.readline().split())
map = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            chicken.append((i,j))
        if map[i][j] == 1:
            home.append((i,j))
# 집과 치킨집 사이의 거리.
min_dis = sys.maxsize
comb = list(itertools.combinations(chicken,m))
min_sum = sys.maxsize
for i in comb: # m개의 치킨 조합들 에 대해서,
    sum = 0
    for k in range(len(home)): # 집들에 대해서
        min_dis = sys.maxsize
        for j in range(len(i)): # 치킨하나하나 에 대해
            dist = abs(home[k][0] - i[j][0]) + abs(home[k][1] - i[j][1])
            if min_dis >= dist:
                min_dis = dist
        sum += min_dis
    min_sum = min(min_sum,sum)
print(min_sum)
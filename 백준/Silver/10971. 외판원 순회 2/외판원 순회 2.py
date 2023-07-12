import sys
from itertools import permutations
n = int(sys.stdin.readline())
c = [i for i in range(n)]
W = []
min_cost = sys.maxsize
for i in range(n):
    W.append(list(map(int,sys.stdin.readline().split())))

for i in permutations(c,n):
    cost = 0
    for k in range(n): # city수 만큼 반복
        start = i[k]
        end = i[(k+1)%n]
        if W[start][end]==0:
            cost+=40000000
        cost +=W[start][end]
    min_cost = min(cost,min_cost)
print(min_cost)
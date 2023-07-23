
import sys
from collections import deque
t = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny <0 or nx>= m or ny >=n:
                continue
            if graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny] = 0

for T in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(k):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1

    total = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                bfs(i,j)
                total += 1
    print(total)
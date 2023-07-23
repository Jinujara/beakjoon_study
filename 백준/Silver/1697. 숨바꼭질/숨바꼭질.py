import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
max = 100001
visited = [0] * max #visited = [0 for _ in range(max)]
def bfs(n):
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for next_node in (v-1,v+1,2*v):
            if 0<= next_node < max and not visited[next_node]: # 방문 했는지 검사 and 범위를 벗어나지 않는지 검사.
                visited[next_node] = visited[v]+1 # 카운트.
                q.append(next_node)
print(bfs(n))
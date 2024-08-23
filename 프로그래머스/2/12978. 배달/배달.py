import heapq

def solution(N, road, K):
    dist = [float('inf')]*(N+1)
    dist[1] = 0 # 시작노드의 거리는 0
    
    adj = [[] for _ in range(N+1)] # 인접노드 그래프
    for a,b,c in road: # 인접노드 추가 a, b 는 노드, c는 거리
        adj[a].append([c,b])
        adj[b].append([c,a])
        
    heap = []
    heapq.heappush(heap, [0,1]) # 거리, 노드
    
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]: # c,n은 node의 각각 거리와 연결노드.
            if cost+c < dist[n]: # 연결노드로 갔을때 노드의 거리가 현재 설정되어있는 거리보다 작으면,
                dist[n] = cost+c # 최단경로이므로 값 변경
                heapq.heappush(heap, [cost+c,n]) #다음연결노드를 힙에 추가. (현재 갱신된 비용보다 크면 힙에 추가하지 않음.)
                
    return len([i for i in dist if i <=K]) # K이하의 마을들의 수
import heapq
def solution(n, edge):
    answer = 0
    
    distance = [int(1e9)] * (n+1)
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    q = []
    # 0번 노드는 없음
    distance[0] = -1
    start = 1
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: # 현재 거리가 기록된 거리보다 크다
            continue
        for neigh in graph[node]:
            cost = dist + 1
            if cost < distance[neigh]:
                distance[neigh] = cost
                heapq.heappush(q, (cost, neigh))
    max_dist = max(distance)
    for i in distance:
        if i == max_dist:
            answer += 1
            
    return answer
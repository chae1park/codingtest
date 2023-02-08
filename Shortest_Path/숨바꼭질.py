# 동빈북 p.390 최단 경로 문제 40 숨바꼭질

import heapq
# 입력예시
n, m = 6, 7
edges = [[3, 6],
         [4, 3],
         [3, 2],
         [1, 3],
         [1, 2],
         [2, 4],
         [5, 2]]
output = [4, 2, 3]

print('expected output', output)


answer = []
INF = 1e9
distance = [INF] * (n+1)
distance[0] = 0

# 양방향 통로 연결 정보를 인접 리스트에 저장
adj = [ [] * (n+1) for _ in range(n+1)]
for v1, v2 in edges:
    adj[v1].append(v2)
    adj[v2].append(v1)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        for neigh in adj[now]:
            if distance[neigh] > (cost + 1):
                distance[neigh] = cost + 1
                heapq.heappush(q, (cost+1, neigh))

dijkstra(1, distance)

cnt = 0
far_cost = max(distance)

# 답의 첫번째 자리: 숨어야 하는 헛간 번호
answer.append(distance.index(far_cost))
# 답의 두번째 자리: 그 헛간까지의 거리
answer.append(far_cost)
# 답의 세번째 자리: 그 헛간과 같은 거리를 갖는 헛간의 개수
for cost in distance:
    if cost == far_cost:
        cnt += 1
answer.append(cnt)

print(answer)
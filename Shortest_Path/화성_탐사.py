# 동빈북 p.388 최단 경로 문제 39 화성 탐사

import heapq

n = 3
costs = [[5, 5, 4],
         [3, 9, 1],
         [3, 2, 7]]
output = 20

n = 5
costs = [[3, 7, 2, 0, 1], 
         [2, 8, 0, 9, 1], 
         [1, 2, 1, 8, 1],
         [9, 8, 9, 2, 0],
         [3, 6, 5, 1, 5]]
output = 19

n = 7
costs = [ [9, 0, 5, 1, 1, 5, 3], 
          [4, 1, 2, 1, 6, 5, 3],
          [0, 7, 6, 1, 6, 8, 5],
          [1, 1, 7, 8, 3, 2, 3],
          [9, 4, 0, 7, 6, 4, 1], 
          [5, 8, 3, 2, 4, 8, 3], 
          [7, 4, 8, 4, 8, 3, 4]]
output = 36

print('expected output', output)

INF = 1e9
distance = [ [INF] * n for _ in range(n) ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start):
    q = []
    cost = costs[start[0]][start[1]]
    distance[start[0]][start[1]] = cost
    heapq.heappush(q, (cost, start))

    while q:
        cost, now = heapq.heappop(q)
        if now == ((n-1), (n-1)):
            break

        for i in range(4):
            nx, ny = now[0]+dx[i], now[1]+dy[i]
            if (nx >=0) and (nx <= (n-1)) and (ny >= 0) and (ny <= (n-1)):
                if (cost + costs[nx][ny]) < distance[nx][ny]:
                    distance[nx][ny] = cost + costs[nx][ny]
                    heapq.heappush(q, (cost + costs[nx][ny], (nx, ny)))

    return distance[n-1][n-1]
start = (0, 0)
answer = dijkstra(start)
print(answer)
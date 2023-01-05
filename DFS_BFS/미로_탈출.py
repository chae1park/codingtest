# 동빈북 p.154 BFS 이론부분
# 이 문제는 시작 지검에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문에
# BFS를 이용했을 때 매우 효과적으로 해결할 수 있다.

from collections import deque



# 입력
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

n, m = 5, 6
graph = [[1,0,1,0,1,0],
         [1,1,1,1,1,1],
         [0,0,0,0,0,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1]]

print('expected output: 10')

# 이동할 네 방향 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                # 밟아나가면서 해당 위치에 최단거리를 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 하단의 최단 거리 반환
    return graph[n -1][m -1]

print(bfs(0,0))
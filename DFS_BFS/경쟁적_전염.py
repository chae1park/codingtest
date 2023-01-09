# 동빈북 p.345 DFS/BFS 문제
from collections import deque
import numpy as np

n, k = 3, 3
graph = [[1,0,2],
         [0,0,0],
         [3,0,0]]

s, x, y = 2, 3, 2

print('expected output: 3')

n, m = 3, 3
graph = [[1,0,2],
         [0,0,0],
         [3,0,0]]
s, x, y = 1, 2, 2

print('expected output: 0')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 로 풀기 (답지 스포를 봐버렸음)

queue = deque()

# 시작점들을 먼저 큐에 넣기
ready = [(i, col) for i, row in enumerate(graph) for j, col in enumerate(row) if graph[i][j] != 0]
print(ready)
for read in ready:
    queue.append(read)
while queue:
    X, Y =queue.popleft()
    value = graph[X+1][Y+1]
    print(X,Y, value)

    for i in range(4):
        nx, ny = (X + dx), (Y + dy)
        if (nx < n) and (nx >=0) and (ny < n) and (ny >= 0):
            if graph[nx][ny] < value:
                graph[nx][ny] = value
                 queue.append((nx, ny))
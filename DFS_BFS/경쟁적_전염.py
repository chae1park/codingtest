# 동빈북 p.345 DFS/BFS 문제
from collections import deque

# 인풋 예시 1
n, k = 3, 3
graph = [[1,0,2],
         [0,0,0],
         [3,0,0]]

s, x, y = 2, 3, 2

output = 3
print('expected output:',output)

# 인풋 예시 2
# n, m = 3, 3
# graph = [[1,0,2],
#          [0,0,0],
#          [3,0,0]]
# s, x, y = 1, 2, 2

# output = 0
# print('expected output:',output)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 로 풀기 (답지 스포를 봐버렸음)
queue = deque()

# 시작점들을 먼저 큐에 넣기 (바이러스의 값, x좌표, y좌표) 저장
ready = [(graph[i][j], i, j) for i, row in enumerate(graph) for j, col in enumerate(row) if graph[i][j] != 0]
# 같은 자리에 바이러스의 값이 더 적은것이 전염되어야 하기때문에 바이러스 값이 적은 것을 먼저 pop할 수 있도록 정렬함 
ready.sort()
for read in ready:
    queue.append(read)

# 제시된 초 만큼 전염 시작
for sec in range(s):
    # 이번 타임에 전염 받아서 다음 타임에 전염시킬 수 있는 위치 좌표 저장할 리스트 
    temp_queue = []

    while queue:
        value, X, Y =queue.popleft()
        value = graph[X][Y]
        for i in range(4):
            nx, ny = (X + dx[i]), (Y + dy[i])
            # 좌표가 맵을 벗어나지 않는지 검사
            if (nx < n) and (nx >=0) and (ny < n) and (ny >= 0):
                # 아직 전염되지 않은 곳인지 검사 후 전염
                if (graph[nx][ny] == 0):
                    graph[nx][ny] = value
                    temp_queue.append((value, nx, ny))
    # 바이러스 값이 적은 것을 먼저 pop할 수 있도록 정렬함 
    temp_queue.sort()
    # 큐에 넣기
    queue.extend(temp_queue)

print(graph[x-1][y-1])
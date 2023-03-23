# 삼성 기출 백준
# https://www.acmicpc.net/problem/15686
from itertools import combinations
from collections import deque

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

n, m = 5, 3
graph = [[0, 0, 1, 0, 0],
        [0, 0, 2, 0, 1],
        [0, 1, 2 ,0, 0],
        [0, 0, 1, 0, 0],
        [0, 0 ,0, 0, 2]]
output = 5

# n, m = 5, 2
# graph = [[0, 2, 0, 1, 0],
#         [1, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [2, 0, 0, 1, 1],
#         [2, 2, 0, 1, 2]]
# output = 10

# n, m = 5, 1
# graph = [[1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0]]
# output = 11

# n, m = 5, 1
# graph = [[1, 2, 0, 2, 1],
# [1, 2, 0, 2, 1],
# [1, 2, 0, 2, 1],
# [1, 2, 0, 2, 1],
# [1, 2, 0, 2, 1]]
# output = 32


# n, m = 5, 4
# graph = [[2, 1, 0, 1, 2],
#          [0, 0, 0, 0, 0],
#          [0, 0, 2, 0, 0],
#          [0, 0, 0, 0, 0],
#          [2, 1, 0, 1, 2]]
# output = 4

print('expected output', output)

# 처음 든 아이디어! 가능한 M개의 치킨집 조합을 뽑아서 다 돌려본다!
# 먼저 M개 조합 고른다음에 포문 돌려서 하나하나씩 그 M개 치킨집 골랐을때의 도시의 치킨 거리의 최솟값을 확인
# 도시의 치킨 거리를 구할때는 최단 거리 dfs 혹은 bfs를 통해 구하기.

# 첫번째 풀이는 BFS로 푼 결과 시간초과가 나왔다. 
# BFS로 푼 다른 풀이들을 보니 bfs를 집이 아닌 치킨을 기준으로 푼 경우가 많았다. (4<=집<=100, 1<=치킨<=13)
# 그리고 최단거리 탐색이라는 틀에 갇혀서 BFS를 썼었는데
# 아주 간단하게 모든 집-치킨과의 거리를 계산해서 최소만 뽑는 방법을 쓰는 풀이도 있어서 놀라웠다.
# 해당 해결방법으로 다시 푼 것이 아래의 코드이다.

answer = 1e9

# 조합 고르기
chickens = [(i, j) for i in range(n) for j in range(n) if graph[i][j]==2]
perm_chickens = list(combinations(chickens, m))
# 치킨집을 다 뺀 기본 맵 생성
city_map = [ [-1] * n for _ in range(n) ]
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 2):
            city_map[i][j] = 0
        else:
            city_map[i][j] = graph[i][j]

houses = [(i, j) for i in range(n) for j in range(n) if graph[i][j]==1]

# 모든 조합에 대해 하나씩 반복문
for perm in perm_chickens:
    perm_chicken_distance = 0
    # 해당 조합의 치킨집을 기록한 맵 생성
    city_map_chicken = [ row[:] for row in city_map]
    for pos_x, pos_y in perm:
        city_map_chicken[pos_x][pos_y] = 2

    for house in houses:
        chicken_distance = 1e9
        for pos_x, pos_y in perm:
            temp = abs(house[0] - pos_x) + abs(house[1] - pos_y)    
            chicken_distance = min(temp, chicken_distance)
        perm_chicken_distance += chicken_distance

    answer = min(perm_chicken_distance, answer)
print('final',answer)






'''
# bfs로 푼 첫번째 풀이
answer = 1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 조합 고르기
chickens = [(i, j) for i in range(n) for j in range(n) if graph[i][j]==2]
# print('chickens',chickens)
perm_chickens = list(combinations(chickens, m))
# print('perm',perm_chickens)
houses = [(i, j) for i in range(n) for j in range(n) if graph[i][j]==1]
# 치킨집을 다 뺀 기본 맵 생성
city_map = [ [-1] * n for _ in range(n) ]
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 2):
            city_map[i][j] = 0
        else:
            city_map[i][j] = graph[i][j]
            
def bfs(x_, y_, dist, visited):
    queue = deque()
    visited.append((x_, y_))
    for i in range(4):
        nx, ny = x_ + dx[i], y_ + dy[i]
        if (0 <= nx < n and 0 <= ny < n) and ((nx, ny) not in visited):
            queue_ = [pos[0] for pos in queue]
            if((nx, ny) not in queue_):
                queue.append(((nx, ny), dist+1))
    while queue:
        (x, y), dist = queue.popleft()

        # 꺼냈는데 치킨 만남
        if (city_map_chicken[x][y] == 2):
            return dist
        # 꺼냈는데 더 갈 수 있음
        if ((x, y) not in visited):
            visited.append((x, y))
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (0 <= nx < n and 0 <= ny < n) and ((nx, ny) not in visited):
                    queue_ = [pos[0] for pos in queue]
                    if((nx, ny) not in queue_):
                        queue.append(((nx, ny), dist+1))

def get_chicken_distance():
    city_chicken_distance = 0
    for x, y in houses:
        chicken_distance = bfs(x, y, dist=0, visited=[])
        city_chicken_distance += chicken_distance
    return city_chicken_distance

# 모든 조합에 대해 하나씩 반복문
for perm in perm_chickens:
    # 해당 조합의 치킨집을 기록한 맵 생성
    city_map_chicken = [ row[:] for row in city_map ]
    for pos_x, pos_y in perm:
        city_map_chicken[pos_x][pos_y] = 2

    perm_chicken_distance = get_chicken_distance()
    answer = min(perm_chicken_distance, answer)

print('final',answer)
'''
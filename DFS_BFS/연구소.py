# 동빈북 p.341 DFS/BFS 문제
# 뭔가 DFS같음

from itertools import combinations
import copy
n, m = 7, 7
graph = [[2, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 1, 2, 0],
         [0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]
output = 27

n, m = 4, 6
graph = [[0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 2],
         [1, 1, 1, 0, 0, 2],
         [0, 0, 0, 0, 0, 2]]
output = 9

n, m = 8, 8
graph = [[2, 0, 0, 0, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 0, 0, 2],
         [2, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
output = 3

print('expected output:',output)


# 우선 dfs 처음 호출을 모든 2마다 함
# 그리고 벽을 세운 이후에 바이러스 퍼진 모습 그리는것은 책의 음료수 얼려먹기 문제와 유사함
# 문제는 벽인 1을 어떤 조건일때 세우느냐인데, 1과 2 세우는걸 탐색하면서 같이 하는걸까?
# 답은... 모든 조합의 3개의 벽을 다 세워보고 (완전탐색) + 바이러스 퍼지는걸 DFS(혹은 BFS)로 구하고 0의 갯수를 계산하는 것이었다.

# 풀 때 어려웠던 점 : 원래 벽/바이러스 정보를 담고있는 graph 변수 이외에 모든 벽을 임시로 세워보는 temp_map 변수를 어떻게 갖고다녀야 하는지 몰랐다.
# 그냥 남들이 짠 코드를 봤을 때는 temp_map 역할을 하는 변수들 밖에서 선언하고 함수마다 안 넣어주기도 하는데, 
# 이거를 정확히 이해하고 구현할 수 있도록 하는 것이 중요한 것 같다. 


# 상, 좌, 하, 우  
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def spread_virus(x, y, temp_map):
    # 바이러스를 퍼지게 하는 함수 (DFS 이용)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                spread_virus(nx, ny, temp_map)


def solve(graph):
    # 벽 만들기
    global result
    for combi in possible_walls:
        temp_map = [ row[:] for row in graph ]

        # 벽 세움
        for wall_x, wall_y in combi:
            temp_map[wall_x][wall_y] = 1

        # 바이러스 퍼지기
        viruses = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 2]
        for virus_x, virus_y  in viruses:
            spread_virus(virus_x, virus_y, temp_map)
            
        # 바이러스가 더 퍼진 후 0의 갯수 개산
        temp_result = [ status for row in temp_map for status in row if status == 0]
        result = max(result, len(temp_result))

    return result 

# 세워야 하는 벽의 개수 k
k = 3
result = -1

possible_empty = [(x, y) for x in range(n) for y in range(m) if (graph[x][y] == 0)]
possible_walls = combinations(possible_empty, k)
answer = solve(graph)
print(answer)
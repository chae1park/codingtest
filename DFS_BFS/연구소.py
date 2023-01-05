# 동빈북 p.341 DFS/BFS 문제
# 뭔가 DFS같음

from itertools import combinations
import copy
# n, m = 7, 7
# graph = [[2, 0, 0, 0, 1, 1, 0],
#          [0, 0, 1, 0, 1, 2, 0],
#          [0, 1, 1, 0, 1, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 1, 1],
#          [0, 1, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 0, 0, 0]]
# output = 27

n, m = 4, 6
graph = [[0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 2],
         [1, 1, 1, 0, 0, 2],
         [0, 0, 0, 0, 0, 2]]
output = 9

# n, m = 8, 8
# graph = [[2, 0, 0, 0, 0, 0, 0, 2],
#          [2, 0, 0, 0, 0, 0, 0, 2],
#          [2, 0, 0, 0, 0, 0, 0, 2],
#          [2, 0, 0, 0, 0, 0, 0, 2],
#          [2, 0, 0, 0, 0, 0, 0, 2],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0]]
# output = 3

print('expected output:',output)


# 우선 dfs 처음 호출을 모든 2마다 함
# 그리고 벽을 세운 이후에 바이러스 퍼진 모습 그리는것은 음료수 얼려먹기로 그리는것과 유사함
# 문제는 1을 어떤조건일때 세우느냐인데, 1과 2세우는걸 같이 탐색하면서 하는걸까?
# 답은... 모든 조합의 3개의 벽을 다 세워보고 (완전탐색) + 바이러스 퍼지는걸 DFS(혹은 BFS)로 구하는 것이었다.


'''
def spread_virus(graph):
    # 바이러스를 퍼지게 하는 함수 (DFS 이용)
    return 
def dfs(x, y):
    # 벽을 세우는 것과 전체 실행함수
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
        
    if graph[x][y] == 0:
        # 여기서 뭔가 바꿈 1로든 2로든.
        graph[x][y] = 1

        dfs(x - 1, y) # 상
        dfs(x, y - 1) # 좌
        dfs(x + 1, y) # 하
        dfs(x, y + 1) # 우
        return True
    # 현재 노드를 이미 방문했다면
    return False

'''
# 상, 좌, 하, 우  
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def spread_virus(x, y):
    # 바이러스를 퍼지게 하는 함수 (DFS 이용)
    # print('in',x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print('nx,ny',nx,ny)
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                # print('전파',(nx, ny))
                spread_virus(nx, ny)
            # 바이러스 전파
            # graph[x][y] = 2
            
            # spread_virus(x - 1, y) # 상
            # spread_virus(x, y - 1) # 좌
            # spread_virus(x + 1, y) # 하
            # spread_virus(x, y + 1) # 우

def solve(graph):
    # 벽 만들기
    global result
    for combi in possible_walls:
        # combi = [(1, 4), (2, 4), (3, 4)]
        print('walls', combi)
        # temp_map = copy.deepcopy(graph)
        temp_map = [ row[:] for row in graph ]

        # 벽 세움
        for wall_x, wall_y in combi:
            temp_map[wall_x][wall_y] = 1

        # 바이러스 퍼지기
        viruses = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 2]
        for virus_x, virus_y in viruses:
            # print('spreading from',viruses[0][0],viruses[0][1])
            spread_virus(virus_x, virus_y)
        # spread_virus(viruses[0][0],viruses[0][1])
        # 바이러스가 더 퍼진 후 0의 갯수 개산
        print('after spreading')
        for row in temp_map:
            print(row)
        temp_result = [ status for row in temp_map for status in row if status == 0]
        print('number of 0 when wall',combi,':',len(temp_result))
        result = max(result, len(temp_result))

        # 그래프 다시 원래 위치로
        for wall_x, wall_y in combi:
            temp_map[wall_x][wall_y] = 0
        # return result 

    return result 

# 세워야 하는 벽의 개수 k
k = 3
result = -1
temp_map = [ row[:] for row in graph ]
# for row in graph:
#     print(row)
possible_empty = [(x, y) for x in range(n) for y in range(m) if (graph[x][y] == 0)]
possible_walls = combinations(possible_empty, k)
answer = solve(graph)
print(answer)
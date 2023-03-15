# 삼성 기출문제 - 아기상어
# https://www.acmicpc.net/problem/16236

from collections import deque

# 문제 이해부터 어렵다! 문제 텍스트만 보고 내가 이해한것은 I라고 한다면 다른 사람들은 E란다!

# 문제의 의도에서는,
#  거리가 가까운 물고기를 모두 다 찾아놓은 다음 제일 위, 왼쪽에 있는 물고기를 선택한것

# 내가 이해한 것은,
#  가까운 물고기를 찾기 위해 제일 위, 왼쪽으로 먼저 이동하면서 제일 가깝기 때문에 먼저 찾아버린 물고기를 선택하고 끝낸다.

# 다만 내가 이해한 방식의 경우 찾는 물고기의 순서가 내가 정해놓은 이동순서(상하좌우, 상좌하우..)에 따라 경로가 달라진다.
# 항상 아래에 있지 않고 오른쪽에 있지 않은 것을 찾아야하기 때문에 이 문제에서는 먼저 다 찾아야 한다...


# input1
# n = 3
# grid = ['0 0 0',
#         '0 0 0',
#         '0 9 0']
# output = 0
# # input2
# n = 3
# grid = ['0 0 1',
#         '0 0 0',
#         '0 9 0']
# output = 3
# # input3
# n = 4
# grid = ['4 3 2 1',
#         '0 0 0 0',
#         '0 0 9 0',
#         '1 2 3 4']
# output = 14
# input4
# n = 6
# grid = ['5 4 3 2 3 4',
#         '4 3 2 3 4 5',
#         '3 2 9 5 6 6',
#         '2 1 2 3 4 5',
#         '3 2 1 6 5 4',
#         '6 6 6 6 6 6']
# output = 60
# # input 5
# n = 6
# grid = ['6 0 6 0 6 1',
#         '0 0 0 0 0 2',
#         '2 3 4 5 6 6',
#         '0 0 0 0 0 2',
#         '0 2 0 0 0 0',
#         '3 9 3 0 0 1']
# output = 48
# # input 6
n = 6
grid = ['1 1 1 1 1 1',
        '2 2 6 2 2 3',
        '2 2 5 2 2 3',
        '2 2 2 4 6 3',
        '0 0 0 0 0 6',
        '0 0 0 0 0 9']
output = 39

grid = [list(map(int,g.split())) for g in grid]
for g in grid:
    print(g)
print('expected output',output)

# BFS로 문제 풀어보기
# 제일 가까운 먹을 수 있는 물고기를 찾아야 함

def bfs_find_fish(q):
    # 먹을 수 있는 가장 가까이 있는 물고기들 정보를 저장할 공간
    candidates = []

    while q:
        pos, size, num_ate, cost = q.popleft()
        # print('pos',pos,'cost',cost)

        for i in range(4):
                nx, ny = pos[0] + dx[i], pos[1] + dy[i]
                if (0 <= nx < n) & (0 <= ny < n) & ((nx, ny) not in visited):
                    # 물고기 사이즈가 같거나 작아야지만 지나가거나 먹을 수 있음
                    if (grid[nx][ny] <= size):
                        # 먹이감 찾음
                        if (grid[nx][ny] != 0) & (grid[nx][ny] != size):
                            if candidates:
                                # 해당 물고기 자리가 최단거리에 있는게 맞는지 검사 후 추가
                                if candidates[-1][3] == cost+1:
                                    candidates.append(((nx,ny), size, num_ate+1, cost+1))
                            # 아직 찾은 물고기가 없다면 제일 거리가 짧아서 처음 찾은 물고기이기 때문에 추가
                            else:
                                candidates.append(((nx,ny), size, num_ate+1, cost+1))
                        # 탐색을 위해 (지나가기 위해) 큐에 정보 저장
                        q.append(((nx,ny), size, num_ate, cost+1))
                        # 이미 지나갔다는 표시하기 위해 리스트에 추가
                        visited.append((nx, ny))
    if candidates:
        candidates = sorted(candidates,key=lambda x: (x[0][0], x[0][1]))
        return candidates[0]
    else: # 먹을 수 있는 물고기가 없을 때
        return (0, -1, -1, -1) # dummy 값 반환

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어의 처음 시작 위치
start = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 9][0]
# print(start)

q = deque()
# 큐에 (시작위치, 사이즈, 먹은 물고기 수, 이동거리) 추가
q.append((start, 2, 0, 0))
visited = [start]
cost_at_ate = 0

# 아기상어 이동할거니까 떠난 자리를 비워 두기
grid[start[0]][start[1]] = 0 

# 먼저 가까운 거리의 물고기들의 위치를 다 찾아서 모아놓음.
# 그 중에 위에 있고 왼쪽에 있는 물고기 하나의 위치를 선별함 (인덱스 숫자 제일 작은 것)
# 그 위치로 이동. 

while True:
    # 제일 가까운 물고기 정보 반환 (여러마리일 경우 위, 왼쪽에 있는 것)
    fish_xy, size, num_ate, cost = bfs_find_fish(q)

    # 먹을 수 있는 물고기 정보가 반환되었을 경우
    if fish_xy:
        # 먹었을 때의 총 이동거리 저장
        cost_at_ate = cost
        # 물고기를 먹어 없어졌으니 그 자리를 비워둠
        grid[fish_xy[0]][fish_xy[1]] = 0
        # 먹은 물고기 개수가 아기 상어 사이즈와 일치하면 사이즈 1 커짐
        if num_ate == size:
            size += 1
            num_ate = 0
            # print('size up', size)
        # 지금 자리부터 다시 탐색 시작할 수 있도록 큐를 초기화
        q = deque()
        visited = [fish_xy]
        # 큐에 시작위치, 사이즈, 먹은 물고기 수, 이동거리 추가
        q.append((fish_xy, size, num_ate, cost))
    # 먹을 수 있는 물고기가 더 이상 없는 경우
    else:
        break
print('final', cost_at_ate)


# # 동빈북 p.352 DFS/BFS 문제 20 감시 피하기

from itertools import combinations
n = 5
graph = [['X','S','X','X','T'],
         ['T','X','S','X','X'],
         ['X','X','X','X','X'],
         ['X','T','X','X','X'],
         ['X','X','T','X','X']]
output = 'YES'

n = 4
graph = [['S','S','S','T'],
         ['X','X','X','X'],
         ['X','X','X','X'],
         ['T','T','T','X']]
output = 'NO'

print('expected output', output)
def check_1direction(data, x, y, d_x, d_y):

    while (0 <= x < n) and (0 <= y < n):
        if data[x][y] == 'S':
            return False
        elif data[x][y] == 'O':
            break # 해당 방향으로 더이상 탐사하지 않음
        else:
            x, y = x+d_x, y+d_y

    # 학생을 찾기 전에 장애물에 부딪혔거나 맵을 벗어난 경우 True 반환
    return True
def check_std(teachers, data, IsAvoided):
    # 상하좌우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    for t_x, t_y in teachers:

        for i in range(4):
            # 각 방향마다 학생이 적발되었는지 검사
            nx = t_x + dx[i]
            ny = t_y + dy[i]
            # 만약 적발되지 않았다면 계속 검사 (적발: False 반환)
            if check_1direction(data, nx, ny, dx[i], dy[i]):
                continue
            # 적발 되었다면 빨리 종료함
            else:
                return False
    # 모든 선생님 기준으로 돌았는데 전부 적발되지 않았다면 그대로 True 반환
    return True


def solution(n, graph):
    # 학생 한 사람이라도 걸리는지 기록하는 변수
    temp_map = [row[:] for row in graph]
    # 설치할 수 있는 장애물의 개수
    k = 3
    # 이것 또한 모든 조합을 찾아보기
    empty = [ (i,j) for i in range(n) for j in range(n) if graph[i][j] == 'X']
    empty_combi = combinations(empty,3)

    for combi in empty_combi:
        IsAvoided = False

        # 장애물 세우기
        for ob_x, ob_y in combi:
            temp_map[ob_x][ob_y] = 'O'
   
        # 학생이 선생님에게 걸리는지 선생님 기준으로 검사 (DFS로 하겠음)
        # 선생님 정보
        teachers = [ (i,j) for i in range(n) for j in range(n) if graph[i][j] == 'T']
        # 학생 감시 피했는지 검사
        IsAvoided = check_std(teachers, temp_map, IsAvoided)

        if IsAvoided == True:
            return "YES"
    return "NO"

print(solution(n,graph))
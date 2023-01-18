# 동빈북 p.355 DFS/BFS 문제 22 블록 이동하기
# 아래 프로그래머스 링크를 통해서 문제 풀기를 권장
# https://school.programmers.co.kr/learn/courses/30/lessons/60063

# 전형적인 BFS 문제라고 함. (다만 현재 위치가 두개이고, 회전이 있다는 것이 다름)

from collections import deque
n = 5
board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]

output = 7
print('expected ouptut',output)

# 회전에 대하여...
# 첫번째 시도는 가로 상태와 세로 상태를 구분해 고려하는 것은 좋았으나, 거기서 위/아래 등 세세한 구분을 하려고 해서 복잡해짐
# 쉽게 푸는 방법은 가로와 세로 상태에서 각각 두 조건만 맞으면 네 회전이 다 가능하다는 것 (가로세로이니 *2해서 8회전 고려)
# 예를 들어 현 상태가 가로일 때 밑이 다 0, 0이어야 왼쪽세로로 회전 & 오른쪽 세로로 회전 가능 
# 현 상태가 세로일때 왼쪽이 다 0, 0 이어야 왼쪽가로위로 회전 & 왼쪽가로아래로 회전 가능..
def rotate(board, x1, y1, x2, y2):
    pass

def get_next_pos(pos, board):
    n = len(board)

    next_pos_list = []
    pos1, pos2 = pos
    x1, y1 = pos1[0], pos1[1]
    x2, y2 = pos2[0], pos2[1]

    # 1. 진행
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx1, nx2 = x1 + dx[i], x2 + dx[i]
        ny1, ny2 = y1 + dy[i], y2 + dy[i]
        
        if (0 <= nx1 < n) & (0 <= nx2 < n) & (0 <= ny1 < n) & (0 <= ny2 < n):
            if (board[nx1][ny1] != 1) & (board[nx2][ny2] != 1):
                next_pos_list.append({(nx1, ny1), (nx2, ny2)})
                
    # 2. 회전 
    # 2-1. 가로일경우
    if x1 == x2: # ((0,1), (0,0))     ---> ((0,0), (1,0)), ((0,1), (1,1))
        # 2-1-1. 가로인데 아래로 갈 수 있는 경우
        if ((x1 + 1) < n) & ((x2 + 1) < n) :
            if (board[x1+1][y1] == 0) & (board[x2+1][y2] == 0):
                next_pos_list.append({(x1, y1), (x1+1, y1)}) # 0,1 1,1
                next_pos_list.append({(x2, y2), (x2+1, y2)}) # 0,0 1,0

        # 2-1-2. 가로인데 위로 갈 수 있는 경우
        if ((x1 - 1) >= 0) & ((x2 - 1) >= 0):
            if (board[x1-1][y1] == 0) & (board[x2-1][y2] == 0):
                next_pos_list.append({(x1, y1), (x1-1, y1)}) 
                next_pos_list.append({(x2, y2), (x2-1, y2)}) 

    # 2-2. 세로일 경우
    if y1 == y2:
        # 2-2-1. 세로인데 오른쪽으로 갈 수 있는 경우
        if ((y1 + 1) < n) & ((y2 + 1) < n):
            if (board[x1][y1+1] == 0) & (board[x2][y2+1] == 0):
                next_pos_list.append({(x1, y1), (x1, y1+1)}) 
                next_pos_list.append({(x2, y2), (x2, y2+1)}) 

        # 2-2-2. 세로인데 왼쪽으로 갈 수 있는 경우 
        if ((y1 - 1) >= 0) & ((y2 - 1) >= 0):
            if (board[x1][y1-1] == 0) & (board[x2][y2-1] == 0):
                next_pos_list.append({(x1, y1), (x1, y1-1)}) 
                next_pos_list.append({(x2, y2), (x2, y2-1)}) 

    return next_pos_list

def solution(board):
    answer = 0
    n = len(board)
    visited = []
    queue = deque()

    # visited를 기록하려면, 두 위치의 순서가 바뀌어도 같은걸로 취급해야 하기 때문에 두 위치를 set형태로 들고다니기
    pos = set({(0,0), (0,1)})
    
    queue.append((pos, 0))
    visited.append(pos)

    while queue:
        cur_pos, cost = queue.popleft()
        # 로봇이 끝에 도달했다면 걸린 시간 cost를 반환
        if (n-1, n-1) in cur_pos:
            return cost
        
        next_pos_list = get_next_pos(cur_pos, board)
        for next_pos in next_pos_list:
            if next_pos not in visited:
                queue.append((next_pos, cost+1))
                visited.append(next_pos)
    return answer

print('result',solution(board))
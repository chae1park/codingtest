# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    answer = 0
    # 최단거리 찾기 (BFS)
    
    n, m = len(maps), len(maps[0])
    
    start = (0, 0)
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        # if (x, y) == (n-1, m-1): # 없어도 효율성 통과함
        #     break
        cost = maps[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < n) & (0 <= ny < m):
                next_cost = maps[nx][ny]
                if ((next_cost != 0) and (cost + 1 < next_cost)) or next_cost == 1:
                    maps[nx][ny] = cost + 1                        
                    q.append((nx, ny))
    for row in maps:
        print(row)
    answer = maps[n-1][m-1]
    if answer == 1:
        return -1
    return answer
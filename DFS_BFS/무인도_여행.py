# 프로그래머스 연습문제 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# DFS로 풀 때 시간초과 에러가 나서
# 프로그래머스에서 recusion limit이 있어서 
# 이걸 설정해주는 코드를 아래와 같이 추가하였더니 해결되었다.

import sys
sys.setrecursionlimit(10**5)

def solution(maps):
    answer = []
    # dfs
    # 탐색 돌면서 식량 총 갯수 반환 
    global n, m
    global food
    global visited
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if (maps[x][y] != 'X') & (not visited[x][y]):
                food = 0
                temp = dfs(x, y, maps)
                answer.append(temp)
                
    if answer:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer
def dfs(x, y, maps):
    global food
    
    if (0 <= x < n) & (0 <= y < m) :
        if (not visited[x][y]) & (maps[x][y] != 'X'):
    
            visited[x][y] = True
            food += int(maps[x][y])
            
            dfs(x-1, y, maps)
            dfs(x+1, y, maps)
            dfs(x, y-1, maps)
            dfs(x, y+1, maps)
    
    return food

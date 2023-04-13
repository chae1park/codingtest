# https://www.acmicpc.net/problem/1012
import sys    
sys.setrecursionlimit(3000)
# DFS를 사용할 때는 RecursionError가 뜰 수 있으니 recursion limit을 지정해주어야 한다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited.append((x, y))
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if (0 <= nx < n) & (0<= ny < m):
            if ((nx, ny) not in visited) & (cab[nx][ny] == 1):
                dfs(nx, ny)
# input 부분
t = int(input())

# 테스트 케이스 수대로 입력
for _ in range(t):
    answer = 0 
    visited = []
    n, m, k = map(int, input().split())
    cab = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        cab[x][y] = 1
    # DFS 탐색 시작
    for i in range(n):
        for j in range(m):
            if ((i, j) not in visited) & (cab[i][j] == 1):
                visited.append((i,j))
                answer += 1
                for idx in range(4):
                    nx = i + dx[idx]
                    ny = j + dy[idx]
                    if (0 <= nx < n) & (0<= ny < m):
                        if (cab[nx][ny] == 1) & ((nx, ny) not in visited):
                            dfs(nx, ny)
    print(answer)


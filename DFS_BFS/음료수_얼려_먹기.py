# 동빈북 p.151 DFS 이론부분
# 입력
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
n, m = 4, 5
graph = [[0, 0, 1, 1, 0],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
print('expected output: 3')

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y) # 상
        dfs(x, y - 1) # 좌
        dfs(x + 1, y) # 하
        dfs(x, y + 1) # 우
        return True
    # 현재 노드를 이미 방문했다면
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
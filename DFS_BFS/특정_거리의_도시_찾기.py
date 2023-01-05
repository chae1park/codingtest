# 동빈북 p.339 DFS/BFS 문제
from collections import deque

n, m, k, x = 4,4,2,1
graph = [[1,2],
         [1,3],
         [2,3],
         [2,4]]
output = 4

# n, m, k, x = 4,3,2,1
# graph = [[1,2],
#          [1,3],
#          [1,4]]
# output = -1

# n, m, k, x = 4,4,1,1
# graph = [[1,2],
#          [1,3],
#          [2,3],
#          [2,4]]
# output = (2,3)

result = [ 0 ] * (n+1)
adj_list = [ [] for _ in range(n+1) ]
for edge in graph:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
print(adj_list)

visited = [False] * (n+1)
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        city = queue.popleft()
        if visited[city] == False:
            # 방문
            visited[city] = True
            result[city] += 1

        for neigh in adj_list[city]:
            if (visited[neigh] == False) and (neigh not in queue):
                queue.append(neigh)
                # 해당 노드에 오기전까지의 거리 = 부모 노드의 거리
                result[neigh] = result[city]

    return result
    

result = bfs(x)

if k not in result:
    print(-1)
else:
    for i, dis in enumerate(result):
        if dis == k:
            print(i) 

print('expected output:', output)
# 동빈북 p.38 최단 경로 문제 38 정확한 순위
N, M = 6, 6
graph = [[1, 5],
         [3, 4],
         [4, 2],
         [4, 6],
         [5, 2],
         [5, 4]]
output = 1
print('expected output', output)

# 처음에 플로이드를 떠올렸으나, 다 하고 앞 뒤로 연결이 있는지 확인하는 걸 생각해내지 못했다.

answer = 0
INF = int(1e9)
matrix = [[INF] * (N+1) for _ in range(N+1)]

# 대각선 원소 0으로 넣기
for i in range(N+1):
    matrix[i][i] = 0

# 매트릭스에 값 대입
for v1, v2 in graph:
    matrix[v1][v2] = 1

# for row in matrix:
#     print(row)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for row in matrix:
    print(row)

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if matrix[i][j] != INF or matrix[j][i] != INF:
            count += 1
    if count == N:
        answer += 1 
print(answer)


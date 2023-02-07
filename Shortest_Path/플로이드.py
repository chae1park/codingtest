# 동빈북 p.385 최단 경로 문제 37 플로이드

# 입력 예시
n, m = 5, 14
graph = [[1, 2, 2],
         [1, 3, 3],
         [1, 4, 1],
         [1, 5, 10],
         [2, 4, 2],
         [3, 4, 1],
         [3, 5, 1],
         [4, 5, 3],
         [3, 5, 10],
         [3, 1, 8],
         [1, 4, 2],
         [5, 1, 7],
         [3, 4, 2],
         [5, 2, 4]]
output = "0 2 3 1 4\n12 0 15 2 5\n8 5 0 1 1\n10 7 13 03\n7 4 10 6 0"
print('expected output')
print(output)


INF = int(1e9)
# 최단거리 테이블 초기화
adj = [[INF] * (n+1) for _ in range(n+1)]
# 거리 정보 저장
for v1, v2, cost in graph:
    # 같은 노선이 여러개 있을 수 있으나 제일 빠른것을 찾기 위함으로 최단 거리인것만 저장
    if adj[v1][v2] > cost:
        adj[v1][v2] = cost

# 자신으로 가는 자리 0으로 초기화
for v in range(n+1):
    adj[v][v] = 0

# 플로이드-워셜 알고리즘을 통한 최단거리 테이블 업데이트
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

# 결과 출력 
# 연결이 없는 경우 0으로 표시를 위해 INF를 우선 0으로 바꿈
graph = [num if num!=INF else 0 for row in graph for num in row ]
for i in range(1, n+1):
    for j in range(1, n+1):
        print(adj[i][j], end=' ')
    print()

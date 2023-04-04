# https://school.programmers.co.kr/learn/courses/30/lessons/49191
def solution(n, results):
    
    # (정확히 순위를 알수 있는 수) = (전체)-(정확히 순위를 모르는 수)
    # 모든 노드에서 최단거리를 구하면서 연결이 아예 없는 노드인 경우 순위를 모른다.
    # 플로이드-워셜 알고리즘으로 모든 노드에서 최단거리 구하기
    
    answer = 0
    INF = int(1e9)
    dist_mat = [[INF]*(n+1) for _ in range(n+1)]
    # 진 선수 -> 이긴 선수
    for win, lose in results:
        dist_mat[lose][win] = 1
    
    # 자신과의 거리는 0으로 초기화
    for i in range(1,n+1):
        dist_mat[i][i] = 0
    
    # 최단거리 구하기
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                dist_mat[a][b] = min(dist_mat[a][k]+dist_mat[k][b], dist_mat[a][b])

    # 모든 다른 선수와 연결이 된 적 있는 선수만 답으로 저장
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if (dist_mat[i][j] != INF) or (dist_mat[j][i] != INF):
                cnt += 1
        if cnt == n:
            answer += 1
        
    return answer

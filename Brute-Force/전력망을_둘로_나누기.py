# https://school.programmers.co.kr/learn/courses/30/lessons/86971    

    # 문제해결시도 1
    # 간선에 for문을 돌면서 해당 간선을 끊었을때 나머지 간선들을 돌면서 단순히 if 문으로 visited 처리
    # 이때 문제점. 간선이 끊겨서 연결이 아예 없는 섬 같은 노드는 무시되었음 (갯수 파악 할 수 없음)
    # -> 따라서 문제해결시도 2로 넘어감 (단, DFS 문제로 푼 풀이를 보니 끊긴 간선부터 갯수를 세면 이 문제를 해결할 수 있었음)
    
    # 문제해결시도 2
    # 아마 간선 정보를 그래프 정보로 만들고, DFS로 풀음.
    # 무슨.. 문제가 있었음. 그래 [1,2], [2,7]에 [6,7] 이 나오면 같은 네트워크인데 [6,7]은 새것으로 취급함.
    # 이것은.. 그래프를 애초에 양방향으로 만들었다면 괜찮았을까??
    
    # 풀이를 본 후 알게된 BFS 해결방법
    # 간선 하나를 끊고 한쪽 노드부터만 BFS를 해서 노드 수를 구하고 한쪽노드수 vs. (전체 - 한쪽노드수) 비교함 
    
    # BFS든 DFS든 *핵심은 노드를 끊고 그 끊은 노드부터 송전탑 갯수를 세서 비교한다는 것!*
    
    # 따라서! 선택한 방법 (DFS)
    # 1. 간선을 loop를 돌며 끊고 (끊은 정보는 집합에 노드정보 넣어서 기억) 
    # 2. 끊은 간선의 양 노드에 대해 dfs를 호출
    # 3. dfs 에서는 호출되어 노드를 visited할때마다 cnt를 세어 반환하여, 
    #    최종적으로 처음 호출한 노드의 갯수를 세주게 됨. 단, dfs를 재귀호출할때 끊어진 간선으로 연결된게 아닌지 검사하는것 잊지 않아야함.
    # 4. 두 노드에 딸린 갯수의 차를 비교하여 최종적으로 제일 작은 경우였을때의 차를 반환 후 종료.
    
def solution(n, wires):        
    answer = 101
    result = 0
    visited = [False] * (n+1)
    wires = sorted(wires)
    
    graph = [ [] for _ in range(n+1) ]
    
    # 그래프 (트리) 만들기
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    def dfs_(node, visited, graph):
        cnt = 0
        visited[node] = True
        cnt += 1
        for adj_node in graph[node]:
            if visited[adj_node] == False:
                if (adj_node not in cut_wire) or (node not in cut_wire): 
                    cnt += dfs_(adj_node, visited, graph)
        return cnt
    
    for wire in wires: # 하나씩 간선 끊어봄
        v1 = wire[0]
        v2 = wire[1]

        # 끊은 간선의 노드 정보 집합에 저장
        cut_wire = set()
        cut_wire.add(v1)
        cut_wire.add(v2)
        
        visited = [False] * (n+1)
        
        # dfs_() 함수는 해당 노드로 부터 시작된(연결된) 노드의 총 갯수를 카운트해 반환
        v1_cnt = dfs_(v1, visited, graph)
        v2_cnt = dfs_(v2, visited, graph)
        
        answer = min(answer, abs(v1_cnt - v2_cnt))
        
    return answer
    

'''
    하나만 끊어졌을때 해보기  

    print('prob #3')
    wires.pop(2)
    print(wires)

    
    # 시도 1
    
    # answer는 두 네트워크 안의 송전탑 개수 차이
    # answer = -1
    answer = n
    # 전력 링크를 하나씩 다 끊어보기
    for i in range(wires): # i 번째 끊기
        print('break',wires[i])
        left_wires = wires[:i] + wires[i+1:]
        print('left wires', left_wires)
        v = 0
        visited = [False] * (n+1)
        # 첫노드 쌍 방문
        visited[left_wires[0][0]] = True
        visited[left_wires[0][1]] = True
        v += 2
        
        
        for j in range(1, len(left_wires)):
            if (visited[left_wires[j][0]]) == False & (visited[left_wires[j][1]]) == False: 
                v -= 1
            if visited[left_wires[j][0]] == True:
                if visited[left_wires[j][1]] == False:
                    visited[left_wires[j][1]] = True
                    v += 1
            elif visited[left_wires[j][1]] == True:
                if visited[left_wires[j][0] == False:
                    visited[left_wires[j][0]] = True
                    v += 1
            
        
        # v1 = 0
        # v2 = 0
        v = 0 
        # 두 네트워크의 송전탑 개수 계산
        # answer = min(answer, abs(v1 - v2))
        answer = min(answer, v)
        print('answer',answer)
    
    # 시도 2 
    def check1(num_net, node1, node2):
        continent = 0 
        if (visited[node1] == False) & (visited[node2] == False): # 1 0
            visited[node1] = True
            visited[node2] = True
            
            print('visited',node1, node2)
            print('first continent')
            continent += 1
            print('result +1')
            num_net.append(1)
            
        elif (visited[node1] == True) & (visited[node2] == False):
            visited[node2] = True
            print('visited', node2)
            num_net[-1] += 1
        elif (visited[node1] == False) & (visited[node2] == True):
            visited[node1] = True
            print('visited',node1)
            num_net[-1] += 1
        print('continent', continent) 
        print('num_net', num_net)
        return num_net
        # if (visited[node1] == True) & (visited[node2] == True): # 알고보니 하나였다 [1,2][3,4][2,3]
        
    num_net = []
    for i in range(len(wires)): # 링크 첫번째부터 방문
        print('go with link',wires[i])
        result = check1(num_net, wires[i][0], wires[i][1])
    print('final num_net',num_net)
    if len(result) == 2:
        print('minimum', abs(num_net[0]-num_net[-1]))
    

'''
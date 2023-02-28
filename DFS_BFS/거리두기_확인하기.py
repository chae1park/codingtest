def solution(places):
    answers = []
    global dx, dy, room_cap
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    room_cap = 5
    
    # DFS로 풀어보겠다
    # P면 dfs 돌기 시작
    # P->O이면 다음에 O가 또 나오면 끝
    # P->X면 끝
    # P->P면 잡았다!
    # P->O->P면 잡았다! (온 방향 아닌 어느 방향이든!)

    for place in places:
        # print(cnt,'th try')
        # print('-'*20)
        # cnt += 1
        answer = check_distance(place)

        if answer == False: # 잘 지킴
            answers.append(1)
        else: # 적발
            answers.append(0)
    return answers
# 입력값 〉	
# ["PXOPX", 
#  "OXOXP", 
#  "OXPOX", 
#  "OXXOP", 
#  "PXPOX"]
# 기댓값 〉	[1] 잘 앉았다
def check_distance(place):
    visited = [ [False]*room_cap for _ in range(room_cap)]
    check = False
    for i in range(room_cap):
        for j in range(room_cap):
             if place[i][j] == "P":
                # print('i j', i, j)
                for k in range(4):
                    nx, ny = i+dx[k], j+dy[k]
                    if (0 < nx < room_cap) & (0 < ny < room_cap):
                        if (not visited[nx][ny]):
                            # print('nx ny', nx, ny)
                            check = dfs(nx, ny, i, j, place)
                            if check: # 부정 적발
                                return check
                                
    return check
def dfs(x, y, i, j, place):
    # print('in dfs x y', x, y, place[x][y])
    if place[x][y] == "O": #PO
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (0 < nx < room_cap) & (0 < ny < room_cap) & ((nx != i) or (ny != j)):
                # print('nx of nx  ny of ny',nx, ny, place[nx][ny])
                if place[nx][ny] == "P": #POP - no
                    # print('returning True')
                    
                    return True
                # elif place[nx][ny] == "O": # POO - good
                # elif place[nx][ny] == "X": # POX - good
                    
    elif place[x][y] == "X":
        return False
    else: # "P"
        # print('returning True')
        return True
    return False
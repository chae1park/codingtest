# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 이 문제의 핵심은 좌표계의 넓이를 2배해서 갈 수 없는 경로를 먼저 잡아주는 것이다.
    answer = 0
    MAX = 102 # 51*2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    map = [ [2] * MAX for _ in range(MAX) ]
    
    # 좌표들을 2배로 바꾸기
    characterX, characterY = characterX*2, characterY*2 
    itemX, itemY = itemX*2, itemY*2
    rectangle = [[x1*2, y1*2, x2*2, y2*2] for x1, y1, x2, y2 in rectangle]

    # 테투리 그리기! : 네모 1로 채우되 내부도 1로 채운다음에 안에를 0으로 바꿈
    # 테두리 + 내부 다 0으로 먼저 그림
    for x1, y1, x2, y2 in rectangle:
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                map[a][b] = 0
    # 내부만 1로 그림            
    for x1, y1, x2, y2 in rectangle:
        for a in range(x1+1, x2):
            for b in range(y1+1, y2):
                map[a][b] = 1
    # character가 item으로 도달하는 최소거리를 bfs로 구하기 
    q = deque()
    q.append((characterX, characterY))
    cost = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (itemX, itemY):
            break
        cost = map[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < MAX) & (0 <= ny < MAX):
                if (map[nx][ny]) == 0: # 테두리인경우 갈 수 있다
                    map[nx][ny] = cost + 1 # 간 거리를 맵에 직접 업데이트
                    q.append((nx, ny))
    answer = (map[itemX][itemY] + 1)//2 # 좌표를 2배했으니 길이를 다시 2배 줄여준다.        

    return answer
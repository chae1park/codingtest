# 동빈북 p.353 DFS/BFS 문제 21 인구 이동

from collections import deque

# # 입력 예시 1 
# N, L, R = 2, 20, 50
# A = [[50, 30],
#      [20, 40]]
# output = 1

# # 입력 예시 2
# N, L, R = 2, 40, 50
# A = [[50, 30],
#      [20, 40]]
# output = 0

# # 입력 예시 3
# N, L, R = 2, 20, 50
# A = [[50, 30],
#      [30, 40]]
# output = 1

# 입력 예시 4
N, L, R = 3, 5, 10
A = [[10, 15, 20],
     [20, 30, 25],
     [40, 22, 10]]
output = 2

# # 입력 예시 5
# N, L, R = 4, 10, 50
# A = [[10, 100, 20, 90],
#      [80, 100, 60, 70],
#      [70, 20, 30, 40],
#      [50, 20, 100, 10]]
# output = 3

print('expected output',output)


def bfs(pos):
     queue = deque()
     united = []
     visited = [[False]*(N+1) for _ in range(N+1)]

     dx = [-1, 1, 0, 0]
     dy = [0, 0, -1, 1]

     queue.append((pos[0], pos[1]))
     visited[pos[0]][pos[1]] = True

     while queue:
          x, y = queue.popleft()
          for i in range(4):
               nx, ny = x + dx[i], y + dy[i]
               if (0 <= nx < N) & (0 <= ny < N):
                    if (L <= abs(A[x][y] - A[nx][ny]) <= R) & (not visited[nx][ny]):
                         united.append((nx, ny))
                         queue.append((nx, ny))
                         visited[nx][ny] = True
     return united
def solution():
     answer = 0
     united_countries = []
     while True: # 종료 조건. 이전 컨트리리스트랑 동일하면?
          # 1.국경선 열기
          start_pos = (0,0)
          print('start_pos',start_pos)
          past_united = united_countries[:]

          # 여기서 연합이 리셋되는게 아니고 국경을 계속 열려있어야 함.
          united_countries = bfs(start_pos) # 여기서 그냥 united를 계속 달아주기? (처음엔 빈리스트)
          print('united',united_countries)
          if len(united_countries) == 0:
               return answer

          united_countries.append(start_pos)
          print(past_united, end='-->')
          print(united_countries)
          if past_united == united_countries:
               break
          population = 0
          for country in united_countries:
               population += A[country[0]][country[1]]

          population = int(population/len(united_countries))
          print('인구이동',population)
          for country in united_countries:
               A[country[0]][country[1]] = population
          # print(A)
          answer += 1

     return answer
print(solution())
# a = [(0,1),(2,3)]
# b = [(2,3)]
# print(id(a),id(b))
# b.append((0,1))
# print(id(a),id(b))
# print(a)
# b.sort()
# print(b)
# print(id(a),id(b))

# print(a==b)
# 국경선 안에 있는 인구들 더해서 평균내고 넣기

# 이거를 또 반복


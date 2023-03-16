# 삼성 기출 백준
# https://www.acmicpc.net/problem/19236
# input1
fish_ = [[] for _ in range(4)]

fish__ = ['7 6 2 3 15 6 9 8',
        '3 1 1 8 14 7 10 1',
        '6 1 13 6 4 3 11 4',
        '16 1 8 7 5 2 12 2']
output = 33

print('expected output',output)
fish__ = [list(map(int, f.split())) for f in fish__]
# print(fish_)
for i in range(len(fish__)):
    for j in range(0,7,2):
        fish_[i].append([fish__[i][j], fish__[i][j+1]])
print(fish_)
# for f in fish:
#     print(f)
print()
'''
1, 2, 3, 4, 5, 6, 7, 8
↑, ↖, ←, ↙, ↓, ↘, →, ↗
1. 처음에 상어가 0,0에서 물고기 먹고 시작
2. 물고기들이 번호순대로 이동
2-2.방향이 막힌 곳이거나 상어인 경우 왼쪽 45도로 돌음
3. 상어가 먹을 수 있는 물고기들을 뽑고 제일 큰 물고기 선택해서 이동
'''
# 이렇게 3차원 리스트 말고 그냥 인덱스와 방향을 가르키게 하면?
# [[(1,1),8], [(0,1),3], [(0,1),1], ...] 이런식으로!!

def num2dir(num, x, y):
    if num == 1:
        return x-1, y
    elif num == 2:
        return x-1, y-1
    elif num == 3:
        return x, y-1
    elif num == 4:
        return x+1, y-1
    elif num == 5:
        return x+1, y
    elif num == 6:
        return x+1, y+1
    elif num == 7:
        return x, y+1
    elif num == 8:
        return x-1, y+1

# 방향이 막힌 곳이거나 상어인 경우 False 반환
def check_safe(nx, ny):
    if 0 > nx or nx >= 4 or 0 > ny or ny >= 4:
        return False
    else:
        if fish[nx][ny] == 17:
            return False
    return True

def move_fish():
    # 번호 순서대로 방향대로 이동 
    for i in range(1,17):
        d = idx_dir[i][1]
        x, y = idx_dir[i][0][0], idx_dir[i][0][1]
        nx, ny = num2dir(d, x, y)
        is_safe = check_safe(nx, ny)
        while not is_safe:
            if d == 1:
                d = 8
            else:
                d -= 1
            nx, ny = num2dir(d, nx, ny)
            is_safe = check_safe(nx, ny)

        # 해당 위치에 있는 물고기와 자리를 바꿈 (방향도 같이 감)   
        obj_fish_idx = fish[nx][ny]
        
        # 바다 속 자리 바꿈
        fish[ny][ny] = i
        fish[x][y] = obj_fish_idx
        # 인덱스 자리 바꿈
        idx_dir[i][0] = (nx, ny)
        idx_dir[obj_fish_idx][0] = (x, y)

def select_max_fish(shark_x, shark_y, shark_dir):
    candidates = []
    nx, ny = num2dir(shark_dir, shark_x, shark_y)
    while 0 <= nx < 4 and 0 <= ny < 4:
        candi_idx = fish[nx][ny]
        candi_dir = idx[candi_idx][1]
        # 물고기 정보 : 물고기 행과 열, 물고기 번호, 물고기의 방향 
        candidates.append(nx, ny, candi_idx, candi_dir)
        nx, ny = num2dir(shark_dir, nx, ny)
    candidates = sorted(candidates, key=lambda x: x[2])
    return candidates[0] # max 번호 가진 물고기 정보만을 반환


answer = 0
idx_dir = [[] for _ in range(18)]
for i in range(4):
    for j in range(4):
        idx_dir[fish_[i][j][0]] = [(i,j), fish_[i][j][1]] # [(x,y), dir]
print('idx map')
print(idx_dir)

fish = [[] for _ in range(4)]
for i in range(4):
    for j in range(4):
        fish[i].append(fish_[i][j][0])
print('real fish')
print(fish)


##### main 시작 #####
# 1. 처음에 상어가 0,0에서 물고기 먹고 시작
# 2. 물고기들이 번호순대로 이동
# 2-2.방향이 막힌 곳이거나 상어인 경우 왼쪽 45도로 돌음
# 3. 상어가 먹을 수 있는 물고기들을 뽑고 제일 큰 물고기 선택해서 이동
# 4. 더이상 먹을 물고기가 없으면 종료인듯

# 처음 상어의 시작
shark_x, shark_y = 0, 0 

# # 상어가 맨 위 왼쪽에서 시작, 방향은 원래 물고기의 것 그대로 변하지 않음 # 상어번호를 17로 지정
# 첫번째 물고기 먹기
first_fish = fish[shark_x][shark_y]
answer += first_fish
shark_dir = idx_dir[first_fish][1] # 상어의 방향을 현재 먹은 물고기것으로
# 첫번째 자리 상어가 차지함
fish[shark_x][shark_y] = 17

while True:
    move_fish()
    fish_x, fish_y, fish_idx, fish_dir = select_max_fish(shark_x, shark_y, shark_dir)
    # 최대 큰 물고기를 뽑았는데 0이면 더이상 물고기 없으므로 상어는 집에 간다.
    if fish_idx == 0:
        break
    # 먹을 물고기와 상어 자리 바꾸고 물고기의 방향도 가져온다 (이전자리 0으로 바꾸기)
    fish[fish_x][fish_y] = 17 # 자리 이동
    # 물고기 방향 업데이트
    shark_dir = fish_dir 
    # 물고기 먹기
    answer += fish_idx
    # 상어 원래 있던 자리 0으로 만들기
    fish[shark_x][shark_y] = 0
    # 새로운 상어 위치로 업데이트
    shark_x, shark_y = fish_x, fish_y
    # 원래 있던 물고기의 정보 지우기
    idx_dir[fish_idx] = [(-1,-1), 0] # 더미값

return answer 



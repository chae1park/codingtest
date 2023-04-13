# 백준 삼전 기출 - 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

# 문제를 잘 읽고 구현만 하면 되는 문제였다! 야호!

# input1
r,c,t = 7, 8, 1
arr = ['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 188

# input2
r,c,t = 7, 8, 2
arr = ['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 188

# input3
r, c, t = 7, 8, 3
arr = ['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 186

# input4
r, c, t = 7, 8, 4
['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 178

# input5
r, c, t = 7, 8, 5
['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 172

# input6
r, c, t = 7, 8, 20
['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 71

# input7
r, c, t = 7, 8, 30
['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 52

r, c, t = 7, 8, 50
['0 0 0 0 0 0 0 9',
'0 0 0 0 3 0 0 8',
'-1 0 5 0 0 0 22 0',
'-1 8 0 0 0 0 0 0',
'0 0 0 0 0 10 43 0',
'0 0 5 0 15 0 0 0',
'0 0 40 0 0 0 20 0']
output = 46

arr = [list(map(int, ar.split())) for ar in arr]
print('expected output', output)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# print('처음 arr')
# for a in arr:
#     print(a)
# print()
purifier = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            purifier.append((i,j))

def validate(x, y):
    if (0 <= x < r) and (0 <= y < c):
        if arr[x][y] != -1:
            return True
    return False

def diffuse(arr):
    arr_copy = [a[:] for a in arr]
    for i in range(r):
        for j in range(c):
            cnt = 0 
            amount = arr[i][j] // 5
            if amount >= 1:
                # print(arr[i][j], amount)
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    if validate(nx, ny):
                        cnt += 1
                        arr_copy[nx][ny] += amount
                # print('cnt',cnt)
                arr_copy[i][j] -= cnt*amount
                # print('result of',arr[i][j], arr_copy[i][j])
    return arr_copy

def purify(arr, row_idx, col_idx):
    arr_copy = [a[:] for a in arr]
    
    # 상부     
    # 아랫쪽 바람 -> 왼쪽 바람 -> 위쪽 바람 -> 오른쪽 바람
    # 아랫쪽 바람
    for idx in range(0,row_idx-1): # 0
        arr_copy[idx+1][col_idx] = arr[idx][col_idx]
    # 왼쪽 바람 (0th row)
    for idx in range(1, c): # 7, 6, ..., 1
        arr_copy[0][idx-1] = arr[0][idx]
    # 위쪽 바람
    for idx in range(1, row_idx+1): # 2, 1
        arr_copy[idx-1][c-1] = arr[idx][c-1]
    # 오른쪽 바람
    for idx in range(1, c-1): # 6, 5, ..., 1
        arr_copy[row_idx][idx+1] = arr[row_idx][idx]
    # 비움 호록
    arr_copy[row_idx][col_idx+1] = 0
    
    # 하부
    row_idx += 1
    # 위쪽 바람 -> 왼쪽 바람 -> 아랫쪽 바람 -> 오른쪽 바람
    # 위쪽 바람
    for idx in range(row_idx+2, r): # 6(r-1), 5
        arr_copy[idx-1][0] = arr[idx][0]
    # 왼쪽 바람 (rth row)
    for idx in range(1, c): # 7, 6, ..., 1
        arr_copy[r-1][idx-1] = arr[r-1][idx]
    # 아랫쪽 바람
    for idx in range(row_idx, r-1): # 3,4,5
        arr_copy[idx+1][c-1] = arr[idx][c-1]
    # 오른쪽 바람
    for idx in range(1, c-1): # 1,2, ..., 6
        arr_copy[row_idx][idx+1] = arr[row_idx][idx]
    # 비움 호록
    arr_copy[row_idx][col_idx+1] = 0
    return arr_copy
row_idx, col_idx = purifier[0][0], purifier[0][1] 
for _ in range(t):
    arr = diffuse(arr)
    # print('after diffusing')
    # for row in arr:
    #     print(row)
    # print()
    arr = purify(arr, row_idx, col_idx)
    # print('after purifying')
    # for row in arr:
    #     print(row)
    # print()
    # break
answer = 0
for row in arr:
    answer += sum(row)
answer += 2 # 공기청정기
print('final',answer)
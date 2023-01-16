# # 동빈북 p.349 DFS/BFS 문제 19 연산자 끼워 넣기

# 입력 받기
# n = int(input())
# A = list(map(int, input().split()))
# n_add, n_sub, n_mul, n_sid = map(int, input().split())

# 입력 예시 1
n = 2
A = [5, 6]
n_add, n_sub, n_mul, n_sid = [0,0,1,0]
output = [30, 30]

# # 입력 예시 2
# n = 3
# A = [3,4,5]
# n_add, n_sub, n_mul, n_sid = [1,0,1,0]
# output = [35, 17]

# # 입력 예시 3
# n = 6
# A = [1, 2, 3, 4, 5, 6]
# n_add, n_sub, n_mul, n_sid = [2,1,1,1]
# output = [54, -24]

print('expected output',output)

# 방법은 1. 순열-완전탐색으로 계산하거나 2. DFS로 풀기가 있다
from itertools import permutations
from collections import deque

min_res = 1e8
max_res = -1e8

# 1. 순열로 가능한 연산자 순서를 다 뽑기
ops_list = []
ops_list.extend(['+'] * n_add)
ops_list.extend(['-'] * n_sub)
ops_list.extend(['*'] * n_mul)
ops_list.extend(['/'] * n_sid)
# print(ops_list)

ops_permute = list(set(permutations(ops_list)))

# 각 연산자 조합에 대해 순차적으로 계산
for ops in ops_permute:
    res = A[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += A[i+1]
        elif ops[i] == '-':
            res -= A[i+1]
        elif ops[i] == '*':
            res *= A[i+1]
        elif ops[i] == '/':
            res = int(res/A[i+1])

    min_res = min(min_res, res)
    max_res = max(max_res, res)

print(max_res)
print(min_res)

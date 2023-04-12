# https://www.acmicpc.net/problem/2644
from collections import deque
# input1
n = 9
tar1, tar2 = 7, 3
m = 7
family = [[1, 2], # 부모, 자식
        [1, 3],
        [2, 7],
        [2, 8],
        [2, 9],
        [4, 5],
        [4, 6]]
output = 3

# input2
# n = 9
# tar1, tar2 = 8, 6
# m = 7
# family = [[1, 2], # 부모, 자식
#         [1, 3],
#         [2, 7],
#         [2, 8],
#         [2, 9],
#         [4, 5],
#         [4, 6]]
# output = -1

# 인풋 부분
# n = int(input())
# tar1, tar2 = map(int, input().split())
# m = int(input())
# family = []
# for _ in range(m):
#     family.append(list(map(int, input().split())))


answer = -1
adj_list = [[] for _ in range(n+1)]

for p, ch in family:
    adj_list[p].append(ch)
    adj_list[ch].append(p)

# bfs
q = deque()
q.append((0,tar1))
visited = [tar1]

while q: 
    chon, now = q.popleft() 
    if now == tar2:
        answer = chon
        break
    for neigh in adj_list[now]:
        if neigh not in visited:
            q.append((chon+1, neigh))
            visited.append(neigh)

print(answer)
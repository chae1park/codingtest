# https://www.acmicpc.net/problem/7568

# n = 5
# info = [[55, 185],
#         [58, 183],
#         [88, 186],
#         [60, 175],
#         [46, 155]]

# output = [2, 2, 1, 2, 5]
# print('expected output', output)

n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))


answers = []
for x, y in info:
    cnt = 0
    for x_, y_ in info:
        if (x < x_) and (y < y_) :
            cnt += 1
    answers.append(cnt+1)
for answer in answers:
    print(answer, end=' ')

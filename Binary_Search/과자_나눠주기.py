# https://www.acmicpc.net/problem/16401

# input1
m, n = 3, 10
snacks = [1,2,3,4,5,6,7,8,9,10]
output = 8

# input2
m, n = 4, 3
snacks = [10, 10, 15]
output = 7

# input3
m, n = 100, 3
snacks = [3,3,3]
output = 0


print('expected output',output)

# m, n = map(int, input().split())
# snacks = list(map(int, input().split()))

# 중간값으로 snacks들의 몫을 구해본다 == 그 중간값이 답일때 나눠줄 수 있는 조카 수
# 이걸 최대값으로 한다!

start = 0
end = 1e9

while (start <= end) :
    cnt = 0
    mid = (start + end) // 2
    if mid == 0:
        answer = 0
        break
    for snack in snacks:
        cnt += snack//mid
    if cnt >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1 
print(answer)



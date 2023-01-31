# 동빈북 p.368 이진 탐색 문제 28 고정점 찾기

# 입력 예시 1
N = 5
nums = [-15, -6, 1, 3, 7] 
output = 3

# 입력 예시 2
# N = 7
# nums = [-15, -4, 2, 8, 9, 13, 15] 
# output = 2

# 입력 예시 3
# N = 7
# nums = [-15, -4, 3, 8, 9, 13, 15] 
# output = -1

print('expected output',output)

# 단 이 문제는 시간 복잡도 O(logN)으로 설계해야 함
# 고정점이 없다면 -1 출력

answer = 0
start, end = 0, (N-1)

while (start <= end):
    mid = (start + end) // 2
    if mid > nums[mid]:
        start = mid + 1
    elif mid < nums[mid]:
        end = mid - 1
    else: # mid == nums[mid]
        answer = mid
        break
if (answer == 0) & (nums[0] != 0):
    print(-1)
else:
    print(answer)
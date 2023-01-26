# 동빈북 p.201 이진탐색 이론부분 문제 3 떡볶이 떡 만들기
N, M = 4, 6
array = [19, 15, 10, 17]
output = 15

print('expected output',output)

answer = 0
start = 1
end = max(array)

while (start <= end):
    # 자르기
    temp = 0
    mid = (start + end) // 2
    for rice in array:
        if rice > mid:
            temp += (rice - mid)

    if temp > M:
        start = mid + 1
    elif temp < M:
        end = mid - 1
    else:
        answer = mid
        break
print(answer)
# 동빈북 p.367 이진 탐색 문제 27 정렬된 배열에서 특정 수의 개수 구하기

N, x = 7, 2
array = [1, 1, 2, 2, 2, 2, 3, 3]
output = 4

# N, x = 7, 4
# array = [1, 1, 2, 2, 2, 2, 3, 3]
# output = -1

print('expected output',output)

answer = 0
start, end = 0, N
while (start <= end):
    mid = (start + end) // 2 
    
    if x > array[mid]:
        start = mid + 1
    elif x < array[mid] :
        end = mid - 1
    else:
        answer += 1
        mid_minus, mid_plus = mid - 1 , mid + 1
        while array[mid_minus] == x:
            answer += 1
            mid_minus -= 1
        while array[mid_plus] == x:
            answer += 1
            mid_plus += 1
        break
if answer == 0:
    print(-1)
else:
    print(answer)
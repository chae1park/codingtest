
# input1
# n, c = 9, 77
# nums = [11, 33, 11, 77, 54, 11, 25, 25, 33]
# output = '11 11 11 33 33 25 25 77 54'
# input2
# n, c = 9, 3
# nums = [1, 3, 3, 3, 2, 2, 2, 1, 1]
# output = '1 1 1 3 3 3 2 2 2'
# input3
n, c = 5, 2
nums = [2, 1, 2, 1, 2]
output = '2 2 2 1 1'

# 입력부분
# n, c = map(int, input().split())
# nums = list(map(int, input().split()))

dicts = {}
for num in nums:
    if num not in dicts:
        dicts[num] = 1
    else:
        dicts[num] += 1
info = sorted(dicts.items(), key=lambda x: -x[1])

answer = ''
for ans, freq in info:
    answer += (str(ans) + ' ') * freq
answer = answer.strip()
print(answer)
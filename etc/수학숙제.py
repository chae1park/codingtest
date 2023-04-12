# https://www.acmicpc.net/problem/2870

# input1
# n = 2
# arr = ['lo3za4', '01']
# output = [1, 3, 4]
# input2
# n = 4
# arr = ['43silos0', 'zita002', 'le2sim', '231233']
# output = [0, 2, 2, 43, 231233]
# input3
n = 4
arr = ['01bond', '02james007', '03bond', '04austinpowers000']
output = [0, 1, 2, 3, 4, 7]

# 인풋 부분
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(input())

answers = []
digits = []
for s in arr: 
    digit = ''
    was_digit = False

    if s[0].isdigit():
        was_digit = True
        digit += s[0]

    for i in range(1, len(s)):
        if s[i].isdigit():
            digit += s[i]
            was_digit = True
        else:
            if was_digit:
                digits.append(int(digit))
                digit = ''
                was_digit = False

    if was_digit:
        digits.append(int(digit))

digits = sorted(digits)
for d in digits:
    print(d)

# https://www.acmicpc.net/problem/2828
n, m = 5, 1
n_apple = 1
apples = [1, 5, 3]
apples = [a-1 for a in apples]
output = 6

n, m = 5, 2
n_apple = 2
apples = [1, 5, 3]
apples = [a-1 for a in apples]
output = 4

# 인풋 받는 부분
# n, m = map(int, input().split())
# n_apple = int(input())
# apples = []
# for _ in range(n_apple):
#     apples.append(int(input())-1)

answer = 0
# basket의 길이가 1인 경우
if n_apple == 1:
    basket = 0
    for apple in apples:
        if apple < basket :
            answer += basket - apple
            # 이동
            basket = apple

        elif apple > basket:
            answer += apple - basket
            # 이동
            basket = apple

# basket의 길이가 2 이상인 경우
else:
    b_left, b_right = 0, m-1

    for apple in apples:
        if b_left <= apple <= b_right:
            continue
        if b_right < apple:
            to_right = apple - b_right
            answer += to_right
            # 이동
            b_left += to_right
            b_right += to_right

        elif b_left > apple:
            to_left = b_left - apple
            answer += to_left
            # 이동
            b_left -= to_left
            b_right -= to_left

# map+lambda를 쓰는것이 리스트 컴프레헨션보다 빠르다!
# basket = list(map(lambda x: x-to_left, basket))

print(answer)
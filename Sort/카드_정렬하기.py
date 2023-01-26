# 동빈북 p.363 정렬 문제 26 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 답을 참고 : https://velog.io/@dding_ji/baekjoon-1715

'''
N = 3
cards = [10, 20, 40]
output = 100

N = 4
cards = [10, 20, 40, 50]
output = 220

print('expected output',output)

# (10 + 20) + (30 + 40) = 100번
# (10 + 20) + (30 + 240) + (70 + 50) = 220번
'''
'''
answer = 0
cards.sort()
answer += (cards[0] + cards[1])
temp = (cards[0] + cards[1])
for i in range(2, N):
    print(i,cards[i])
    answer += (temp + cards[i]) # (10+20)+(10+20)+40 # (10+20)+(10+20+40)+(10+20)+(10+20+40)+70
    temp += cards[i] # 10+20+40 # 20 + 40 + 50
    print(answer)
    print(temp)
print(answer)
'''
'''
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
answer = 0
cards.sort()

if N == 1:
    answer = 0
else:
    answer += (cards[0] + cards[1])
    temp = (cards[0] + cards[1])
    for i in range(2, N):
        # print(i,cards[i])
        answer += (temp + cards[i]) # (10+20)+(10+20)+40 # (10+20)+(10+20+40)+(10+20)+(10+20+40)+70
        temp += cards[i] # 10+20+40 # 20 + 40 + 50
        # print(answer)
        # print(temp)
print(answer)
'''
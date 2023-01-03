# 프로그래머스 연습문제 > 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# Idea: 1일차부터 하루씩 늘려가며 (첫번째 for문) 10일씩 할인품목 카운터를 씌운 다음,
#       이때 원하는 상품과 그 수가 일치하는지 검사하고 그 여부를 boolean 변수에 저장 (두번째 for문)
#       검사할 때 한 품목이라도 수가 모자라면 즉시 종료하며 boolean 값을 int로 바꿔서 수를 세어줌 (True-> 1, False->0)

from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = 10
    want_dict = { want[i]:number[i] for i in range(len(want))}

    for i in range(len(discount)-d+1):
        isSatisfied = True
        cntr = Counter(discount[i:i+d])
        for item, quantity in want_dict.items():
            if cntr[item] < quantity:
                isSatisfied = False
                break
        answer += int(isSatisfied)

    return answer
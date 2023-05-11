# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    if k == len(enemy): # 모든 공격에 무적권 사용할 수 있음
        return k
    for en in enemy:
        heapq.heappush(q, -en) # 최대힙
        n -= en # 완호의 병사로 이번 라운드 적 상대
        
        if n < 0: # 완호의 병사가 남아있지 않을 때
            if k > 0: # 무적권 기회가 있을 때
                mu = heapq.heappop(q) # 그동안 상대했던 적 중 제일 큰 라운드의 적 수를 가져온다
                n -= mu # 완호 병사 수 회복
                k -= 1 # 기회 1 소진
            else:
                return answer # 적의 수도 많고 무적권 기회도 없을 때 종료
        answer += 1 # 해당 라운드 통과
    return answer
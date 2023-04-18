# https://school.programmers.co.kr/learn/courses/30/lessons/42628#

import heapq
def solution(operations):
    # max값과 min값을 관리해야해서 두 개의 힙을 사용함.
    # 다른 풀이들을 살펴보니 배열에서 매번 sort해도 풀리고, 힙 하나쓰고 heaqp.nlargest(n, list) 함수를 써도 구현이 가능하다.
    answer = []
    q = []
    max_q = []

    for op in operations:
        
        order = op.split()[0]
        val = int(op.split()[1])
        
        if order == 'I':
            heapq.heappush(q, val)
            heapq.heappush(max_q, val*(-1))
            
        elif order == 'D':
            if val == -1:
                if q:
                    min_val = heapq.heappop(q)
                    max_q.remove(min_val*(-1))
                    
            elif val == 1:
                if q:
                    max_val = heapq.heappop(max_q)
                    q.remove(max_val*(-1)) 
            
    if len(q) < 1 :
        answer = [0, 0]
    else:
        # answer = [q[-1], q[0]]
        answer = [max(q), min(q)]
        
    return answer
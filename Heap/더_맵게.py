import heapq
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    # heapq.heappush(list, "element") # 오름차순
    # heapq.heappop(list) # 앞에꺼 사라짐
    '''
    *문제*
    scoville 리스트에는 음식들의 스코빌 지수 (int)가 들어있음
    이 모든 음식들의 스코빌 지수가 K 이상이 되도록 제일 적은 스코빌 지수와 두번째로 제일 적은 스코빌 지수*2 를 더해서 리스트에 다시 넣음
    (이 과정을 두 음식을 섞는다고 표현)
    두 음식을 몇번 섞어야 리스트의 모든 음식의 스코빌 지수가 K 이상이 되는지 그 횟수를 출력하면 됨.
    단, 아무리 섞어도 K 이상이 되지 않는다면 -1를 반환
    
    *푼 방법*
    리스트를 힙처럼 만듬. 숫자 하나씩 제일 적은 것부터 pop해서 그게 K 이상인지 확인 (맞으면 바로 리턴)
    K 이상이 아니라면 두번째 적은 것을 또 꺼내서 계산한 후 힙 heappush 함. 그리고 섞은 횟수를 +1 함.
    위의 과정을 힙의 원소가 하나 남을 때까지 반복.
    루프를 나왔을 때 마지막에 남은 원소가 K 이상임을 만족했는지 검사 후 그에 따른 답을 출력
    '''
    
    answer = 0
    scoville = sorted(scoville)
    
    while (len(scoville) >= 2):
        least_spicy = heapq.heappop(scoville)
        if least_spicy >= K:
            return answer # 중간에 다 만듬
        else:
            less_spicy = heapq.heappop(scoville)
            new_least_spicy = least_spicy + (2 * less_spicy)
            heapq.heappush(scoville, new_least_spicy)
            answer += 1
    
    # 영원히 못만듬
    if (len(scoville) == 1) & (scoville[0] < K):
        answer = -1 
    
    return answer
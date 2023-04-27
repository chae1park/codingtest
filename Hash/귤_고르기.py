# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    # 서로 다른 종류가 최소가 되도록 k개만 남기는 것
    
    # Greedy & Hash 문제로 풀었음.
    # 제일 적은 수의 귤부터 순서대로 빼기!
    
    answer = 0
    n = len(tangerine)
    
    # 귤 갯수 딕셔너리에 저장
    tans = {}
    for t in tangerine:
        if t not in tans:
            tans[t] = 1
        else:
            tans[t] += 1
    
    # 갯수가 적은 것부터 제외시키기 위해 오름차순으로 정렬
    tans = sorted(tans.values())
    
    # 귤 빼기 (cnt 개수만큼)
    cnt = n - k
    
    idx = 0 
    while (cnt > 0) and (idx < n):
        # 이미 다 수량만큼 뺀 귤종류는 다음으로 넘어감
        if tans[idx] == 0:
            idx += 1
            continue
        
        if tans[idx] <= cnt:
            # 귤 빼기
            cnt -= tans[idx]
            tans[idx] = 0
            
        else: 
            cnt = 0
            # tans[idx] -= cnt # 안해도 답에 지장없음 
            break
            
    for t in tans:
        if t != 0:
            answer += 1
    return answer
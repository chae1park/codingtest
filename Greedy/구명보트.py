# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    # idea는 제일 작은것과 제일 큰것을 합해서 함께 빼기 다만 그 합이 limit 이하면 큰것을 뺀다
    sm_idx, bg_idx = 0, (len(people)-1)
    
    people.sort()
    
    while sm_idx <= bg_idx:
        
        if (people[sm_idx] + people[bg_idx]) <= limit:            
            sm_idx += 1
            bg_idx -= 1
            answer += 1
            
        else:
            bg_idx -= 1
            answer += 1
            
    return answer
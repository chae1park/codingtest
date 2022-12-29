# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    
    # 1. 여벌 체육복을 가져온 학생이 체육복을 도난당해서 (-1) 1개가 된다면 체육복 못빌려줌
    #    lost 와 reserve 공통인 학생을 reserve, lost에서 없앰
    
    #    1) 리스트를 집합화
    lost_pool = set(lost)
    reserve_pool = set(reserve)
    #    2) 공통인 번호를 찾음
    reserve_and_lost = lost_pool.intersection(reserve_pool)
    #    3) 각자 집합에서 뺌
    lost_pool -= reserve_and_lost
    reserve_pool -= reserve_and_lost
    
    #    4) 집합을 다시 리스트화
    lost = sorted(list(lost_pool))
    reserve = list(reserve_pool)
    
    # 도난당한 사람을 뺀 참석 가능 학생 수
    answer = n - len(lost)
    
    # 체육복 빌려준 사람을 저장하는 리스트
    occupied = []
    
    # 2. 체육복 없는 사람의 앞과 뒤를 검사해서 체육복 빌릴수 있으면 빌려준 사람을 occupied에 저장
    for i in lost:
        # lost 안의 원소가 작은 순부터 나오기 때문에 수의 앞부터 검사
        if (i-1) in reserve and (i-1) not in occupied :
            occupied.append(int(i-1))
        elif (i+1) in reserve and (i+1) not in occupied :
            occupied.append(int(i+1))
        else:
            continue
            
    # 3. 체육복을 빌려준 사람 수 = 체육복 다행히 빌린 사람수 를 참석가능한 사람 수에 추가해줌
    answer += len(occupied)
    
    return answe
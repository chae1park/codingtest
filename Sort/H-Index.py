def solution(citations):
    answer = 0
    cumsum_cite = 0
    # 해시 방식으로 풀기.
    # 즉, 최대 인용 수 만큼의 길이를 가진 리스트를 만들어 해당 인용 수만큼 인용한 논문의 갯수를 담음
    
    # 10000회 (인덱스) 이용된 논문 갯수 (논문 갯수) 담김 
    num_list = [0] * 10001  
    
    for cite in citations:
        num_list[cite] += 1
        
    for i in range(10000, -1, -1):
        cumsum_cite += num_list[i]
        if cumsum_cite >= i:
            answer = i
            return answer
        
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return int(5 * len(cities))
    
    q = []
    for City in cities:
        city = City.lower() # 도시이름을 전부 소문자로 통일
        if city not in q: # Miss
            answer += 5
            if len(q) == cacheSize: # cache가 꽉찼다면 오래된 걸 빼고 넣어줌
                q.pop(0)
            q.append(city)
        else: # Hit
            answer += 1
            # cache안에 있는 해당 도시 지우고 최근 자리로 다시 넣어야 함.
            idx = q.index(city)
            q.pop(idx)
            q.append(city)
    return answer
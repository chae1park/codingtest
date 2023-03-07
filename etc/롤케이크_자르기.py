# 프로그래머스 코딩테스트 연습문제 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265
def solution(topping):
    # 해당 문제는 시간 정확도를 통과하기 위해 데이터를 어떤 자료에 저장할 것인가가 중요했고, 
    # 반복문을 어떤 방식으로 돌아야 하는지도 시간 정확도를 위해 고민해야 한다.
    
    answer = 0
    n = len(topping)
    # 해당 문제는 딕셔너리와 set을 이용해 두가지로 토핑을 나눈다
    rear = set()
    front = {}
    
    # 1.처음 딕셔너리에 토핑의 종류를 키로 하여 토핑의 갯수를 값으로 전부 저장한다
    for t in topping:
        front[t] = front.get(t, 0)
        front[t] += 1
        
    # 2.반복문을 돌며 하나씩 토핑을 set으로 옮기면서 (딕셔너리에선 지움) 토핑의 가지 수가 일치하는지 비교한다.
    for t in topping:
        rear.add(t)
        front[t] -= 1
        # 3.정확한 토핑 가지 수 비교를 위해 해당 토핑 종류가 다 옮겨져 갯수가 0이 된 경우 딕셔너리에서 키값을 아예 지워야 한다.
        if front[t] == 0:
            del front[t]
        if len(rear) == len(front):
            answer += 1
    return answer
    '''
    
    # 처음 idea! 
    # for문을 돌며 처음부터 슬라이싱해서 두 그룹으로 나눈후
    # set으로 중복제거하여 그 가지수가 같으면 정답에 count +1한다.
    # 그 결과 테스트는 통과했지만 제출했을 때 시간초과가 많이 났다. (슬라이싱이 시간이 많이 걸리는 작업인 것 같다.)
    
    # 처음 짠 코드
    for mid in range(1,len(topping)-1):
        old = topping[:mid]
        young = topping[mid:]
        if len(set(old)) == len(set(young)):
            answer += 1
            
    if answer == -1:
        return 0
    else:
        return answer + 1
    return answer
    '''
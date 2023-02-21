# 프로그래머스 연습문제: 뒤에 있는 큰수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    answer = []
    
    # 처음 풀이법!
    # 주어진 매개변수를 순서대로 돌면서 이중 포문으로 그 뒤부터 탐색해서
    # 해당 수보다 크면 답에 그 큰 수를 추가하고 컨티뉴.
    # 전체 크기가 최대 1e6인데 이중 포문이니 당연히 결과는
    # 절반 이상이 시간초과가 났다.
    
    # 두번째 풀이!
    # 최신것만 보면 되니까 stack 구조를 사용하기로 함
    # 테스트 케이스를 적어놓고 상상해보며 언제 stack에서 비교하며 
    # 현재 수보다 작으면 현재수가 제일 가깝고 크니 작은 수는 pop을 하고
    # 현재 수보다 클 때 그 수를 남겨놓고 답에 추가한다. 그리고 현재 수를 stack에 추가하고 마친다
    
    # ***중요하게 깨달은 사실!***
    # 역순 for문 돌았기 때문에 답을 list.append한 다음 마지막에 한꺼번에 뒤집어주면 되는데,
    # 나는 역순이니까 답 리스트에 list.insert(0, 답) 이런식으로 저장했다.
    # 이것만 잘못했는데 절반의 문제가 시간초과가 났다.
    # 알고리즘을 맞아놓고 이런 사소한 것으로 테스트 통과를 못할 수도 있다니 
    # 무조건 append()를 쓸 수 있다면 이것을 쓰는 방향으로 가야겠다.
    
    ls = []
    numbers = numbers[::-1]
    
    for i, num in enumerate(numbers):
        
        if num == 1000000:
            answer.append(-1)
            ls.append(num)
            continue
            
        while ls : # ex) 더나중: 76 나중: 70 현재: 75 큐에는 [1, 2, 20, 75, 80, 100]
            if num >= ls[-1]: # 현재 수보다 큐에 작은 것들이면
                ls.pop() # 날림. 어차피 현재 수인 num이 그 자리에 들어가서 큰 수 역할이 됨
            else:
                break
                
        if not ls: # 다 돌았는데 현재 수가 가장 크다면
            answer.append(-1)
        else: # 현재 수보다 큰 수를 찾았다면
            it = ls[-1] # 나보다 큰 이 친구는 남김
            answer.append(it) 
            
        ls.append(num)
        
    answer = answer[::-1]
    return answer

    # 처음 방법 풀이 코드 (시간초과로 실패)
    # for i, num1 in enumerate(numbers):
    #     if num1 == 1000000:
    #         answer.append(-1)
    #         continue
    #     for num2 in numbers[i+1:]:
    #         if num2 > num1:
    #             answer.append(num2)
    #             break
    #     if len(answer) == i:
    #         answer.append(-1)
    

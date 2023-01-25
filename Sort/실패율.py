# 동빈북 p.361 정렬 문제 25 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889


import itertools  

def solution(N, stages):
    answer = []
    
    # 처음 생각했던 풀이!
    # - 모든 유저들의 현황이 담긴 stages를 하나씩 돌면서
    # - N개의 리스트에다가 그 해당 n번째 단계를 깬 사람들의 수를 더해주고
    # - 그 리스트로 한꺼번에 실패율 계산 :  ((전 단계 깬사람)-(이번 단계 깬사람)) / 전 단계 깬사람
    # 하지만 제출 후 런타임 에러 27개중 8개가 떠서, 다른 풀이를 본 후 다음 조건을 가지고 다시 풀어보기로 함
    
    # 새로 세운 조건
    # 1. for문은 stages 말고 N번만 돈다
    # 2. 실패율을 바로 계산하게 해본다
    # 3. 1&2 충족시에도 런타임 에러가 난다면 계산 안해도 되는 케이스를 생각해 앞에다 조건을 걸어놓는 부분을 추가한다.
    
    # 위의 1&2를 충족한 코드를 작성했으나 (심지어 for문을 쓰지않았다) 처음 생각했던 풀이와 똑같은 종류와 갯수의 런타임 에러가 났다.
    # 해당 런타임 에러를 해결하기 위해 중요한 것은 for문을 몇 번 도느냐 보다는 조건을 하나 추가하는 것이었다.
    
    user_len = len(stages)
    cnts = [ stages.count(i) for i in range(N+1)]
    accs = list(itertools.accumulate(cnts))
    
    # 케이스 추가한 코드
    status = [ (cnts[i] / (user_len-accs[i-1]), i) if cnts[i] != 0 else (0,i) for i in range(1, N+1) ]
    # 이전 코드
    # status = [ (cnts[i] / (user_len-accs[i-1]), i) for i in range(1, N+1)]

    status = sorted(status, key=lambda x: -x[0])
    answer = [ tup[1] for tup in status]
    
    return answer
    
    '''
    # 처음 생각한 풀이
    status = [ 0 for _ in range(N+1)] 
    for stage in stages:
        for i in range(stage-1, -1, -1):
            status[i] += 1
    failures = [ ((status[i]-status[i+1]) / status[i], ((i+1))) for i in range(N)]
    failures = sorted(failures, key=lambda x: -x[0])
    answer = [ tup[1] for tup in failures]
    return answer
    
    '''
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print('expected output', '[3,4,2,1,5]')

print(solution(4, [4, 4, 4, 4, 4]))
print('expected output', '[4,1,2,3]')

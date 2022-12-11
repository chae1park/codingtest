
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

'''
처음 나의 풀이법! 현재 상태에서 가능한 리스트에 있는 모든 원소들을 선택했을 때 소요 시간 다 계산해서 그 중 짧은것들을 선택하도록 함
 -> 풀리지 않았다.

힌트 보고 난 후의 풀이법
처음에는 요청시간 제일 빠른거로 시작하고, 그 다음부터 현재 상태(시간)에서 이전에 들어온 요청된 것 중 실행시간이 적게 걸리는것부터 선택하기
인트는 실행 후 현재 상태 시간 계산을 잘하는 것, 이전에 요청된 작업들을 소요시간 적은 순으로 정렬해서 작업때마다 갱신하는 것, 이전에 요청된 작업이 없을 경우를 처리해주는 것.
'''
        
def solution(jobs):
    answer = 0
    n = len(jobs)
    
    # 작업 목록을 요청 순으로 정렬
    jobs = sorted(jobs)
    
    # 첫 요청된 작업부터 수행
    execute = jobs.pop(0)
    
    # 첫 작업의 끝난 시간 계산
    curr_complete = execute[0] + execute[1]
    
    # 첫 작업의 소요 시간 더함
    answer += execute[1]
    
    # 모든 요청을 소모할때 까지 루프
    while jobs: 
        # 현재 시간 이전에 요청된 작업들의 리스트 갱신
        requested = [ job for job in jobs if job[0] <= curr_complete]
        
        # 이전에 요청된 작업들이 존재할 때
        if requested:
            # 요청된 작업들의 작업시간이 적은 순으로 정렬
            requested = sorted(requested, key=lambda x:x[1], reverse=True)
            # 제일 시간 적은 작업을 꺼내서 실행
            execute = requested.pop()
            # 작업 소요 시간 계산 후 더해줌 (실제 작업시간 + 현재 시간까지 기다린 시간)
            answer += execute[1] + abs(curr_complete - execute[0])
            # 해당 작업 완료 후의 현재 시간 계산
            curr_complete = curr_complete + execute[1] 
            # 작업 마쳤으니 jobs 리스트에서 삭제
            jobs.remove(execute)
            
        # 이전에 요청된 작업이 없을때    
        else: 
            # 남은 작업들 중 제일 빠른 요청시간으로 현재 시간을 설정 후 마저 루프돌 수 있게 함. 
            curr_complete = jobs[0][0]
            
    # 작업 소요시간들의 합을 작업 수로 나눠서 평균을 내줌
    answer /= n
    # 소수점을 버리고 반환
    return int(answer)
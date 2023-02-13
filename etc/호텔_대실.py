# 프로그래머스 연습문제 호텔대실
# https://school.programmers.co.kr/learn/courses/30/lessons/155651#

# IDEA
# 1. 문자열 형태로 주어지는 시간을 분 단위의 정수 형태로 변환 -> 10분 후를 조작할 수 있음
# 2. 대실한 종료시간 (+청소 10분) 현황을 가지는 리스트로 비교하면서 새 방을 추가할지 아닐지 결정
# 3. 이 때 종료시간 리스트의 제일 빨리끝나는 시간과 비교해 Greedy 하게 방을 넣을 수 있도록 함.

def time2int(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(book_time):
    answer = 0
    book_time.sort()
    status = []
    for book in book_time:
        start = time2int(book[0])
        end = time2int(book[1])
        if status:
            if(min(status) <= start):
                idx = status.index(min(status))
                status[idx] = end+10
                continue
                
            else:
                status.append(end+10)
                answer += 1
        else:
            status.append(end+10)
            answer += 1
            
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math
def time2int(tm):
    h, m = map(int, tm.split(":"))
    return (60 * h) + m
def solution(fees, records):
    answer = []
    # fees: 기본시간,기본요금,단위분,추가요금
    b_time, b_fee, a_time, a_fee = fees 
    
    # 0. 시간을 분단위 숫자로 변환하기
    # 1. 입출차 정보를 차 번호 기준으로 저장해놓기
    info = {}
    car_fees = {}
    
    for rec in records:
        tm, car, io = rec.split()
        tm = time2int(tm)
        if car in info:
            info[car].append([tm, io])
        else:
            info[car] = [[tm, io]]
    # 1-2. 출차 기록이 없는 차의 경우 "23:59", OUT을 더해줌
    out_time = time2int("23:59")
    for car in info:
        if len(info[car]) % 2 == 1:
            info[car].append([out_time, "OUT"])
    
    # 2. 차 번호대로 요금 계산 후 딕셔너리에 저장
    for car, recs in info.items():
        st = 0
        for rec in recs: # [1459, "IN"]
            if rec[1] == "OUT":
                st += rec[0]
            elif rec[1] == "IN":
                st -= rec[0]
        # 요금 계산
        if st <= b_time:
            money = b_fee
        else:
            money = b_fee + (math.ceil((st - b_time) / a_time) * a_fee)
        car_fees[car] = money
        
    # 3. 차 번호대로 정렬 후 반환
    answer = sorted(car_fees.items(), key=lambda x: x[0])
    answer = [ans[1] for ans in answer]
    
    return answer
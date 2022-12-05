# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 프로그래머스 - 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    current_num = arr[0]
    n = len(arr)
    answer.append(current_num)
    
    for i in range(1, n):
        if current_num == arr[i]:
            continue
        else:
            current_num = arr[i]
            answer.append(current_num)
        
    return answer
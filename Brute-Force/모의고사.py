# https://school.programmers.co.kr/learn/courses/30/lessons/42840#


def solution(answers):
    answer = []
    num_supo = 3
    supo_list = [0] * num_supo
        
    patt1 = [1,2,3,4,5]
    patt2 = [2,1,2,3,2,4,2,5]
    patt3 = [3,3,1,1,2,2,4,4,5,5]
    
    patt1_len = len(patt1)
    patt2_len = len(patt2)
    patt3_len = len(patt3)
    
    for i, ans in enumerate(answers): 
        if patt1[i % patt1_len] == ans:
            supo_list[0] += 1
        if patt2[i % patt2_len] == ans:
            supo_list[1] += 1 
        if patt3[i % patt3_len] == ans:
            supo_list[2] += 1
    
    max_supo = max(supo_list)
    answer = [idx+1 for idx, val in enumerate(supo_list) if val == max_supo]
    
    return answer
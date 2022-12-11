# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    width = 0
    height = 0
    
    for size in sizes:
        # 가로 세로 그대로 기존 지갑 사이즈에 들어가는지 검사
        if size[0] > width:
            temp_w1 = size[0]
        else: 
            temp_w1 = width
        if size[1] > height:
            temp_h1 = size[1]
        else:
            temp_h1 = height
        
        # 명함을 90도 돌렸을 때 기존 지갑 사이즈에 들어가는지 검사
        if size[1] > width:
            temp_w2 = size[1]
        else:
            temp_w2 = width
        if size[0] > height:
            temp_h2 = size[0]
        else:
            temp_h2 = height
        
        # 명함을 그대로 두었을 때와 90도 돌렸을 때의 지갑 사이즈 중 면적이 더 최솟값인 것을 선택
        if (temp_w1 * temp_h1) <= (temp_w2 * temp_h2):
            width = temp_w1
            height = temp_h1
        else: 
            width = temp_w2
            height = temp_h2  
            
    answer = int(width * height)
    return answer
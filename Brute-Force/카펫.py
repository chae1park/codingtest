# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    gobs = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            gobs.append([yellow//i, i])
    for width, height in gobs:
        if (2*(width + height) + 4) == brown:
            return [width+2, height+2]
    return answer
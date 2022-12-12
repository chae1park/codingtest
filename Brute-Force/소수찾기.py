# https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 참고 링크 (소수 검사하기)
# - https://seongonion.tistory.com/43


# 흩어져있는 숫자들의 모든 조합을 구할때 permuatations(list, num_permutes) 사용
from itertools import permutations

def solution(numbers):
    answer = 0
    permutes = []
    
    # 문자열로 되어있는 숫자를 한자리씩 뗌
    strings = [num for num in numbers]
    # 한자리수 부터 n(문자열 총 갯수) 자리의 순열조합을 구하여 리스트에 넣음 
    for i in range(1, len(numbers)+1):
        permutes += list(permutations(strings, i))
    # 튜플 형태로 반환된 순열조합을 합침
    permutes = [''.join(tups) for tups in permutes]
    # 합쳐서 만들어낸 숫자가 아직 문자열 타입이므로 자연수 형태로 바꿔주고 중복을 제거함.
    # 이때 1과 0은 소수가 아니므로 미리 거름
    permutes = list(set([int(num) for num in permutes if int(num) > 1])) 
    
    # 하나씩 소수인지 검사
    for num in permutes:
        isSosu = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isSosu = False
        answer += int(isSosu)
        
    return answer
'''
*idea*
원소는 1000 이하의 수로 구성되어 있으므로 최대 세자리 수다.
9 > 99 > 998 이렇게 나와야 한다
세자리 수이므로 999 > 999999 > 998998998 이런식으로 문자열 * 3로 하면 가능
'''

def solution(numbers):
    answer = ''
    numbers_str = [str(number)*3 for number in numbers]    
    numbers_str = sorted([str(number) for number in numbers], key=lambda x:x*3, reverse=True)
    answer = ''.join(numbers_str)
    answer = str(int(answer))
    
    return answer
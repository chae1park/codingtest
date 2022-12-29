# https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3

# from itertools import permutations # 중복 없는 순열
# from itertools import combinations # 중복 없는 조합
# from itertools import product # 중복 있는 순열
# from itertools import combinations_with_replacement # 중복 있는 조합


from itertools import product

def solution(word):
    answer = 0
    # print('A0000' < 'AAAAA') # True 
    # 빈 공간 표현 위해 문자열보다 앞 순위고 더미 값인 '0' 대입
    # dictionary 크기는 3905
    
    # *문제 해결 방법*은 가능한 단어의 딕셔너리를 조합으로 만들고 정렬한다음 (총 3905 개 밖에 없음)
    # 인풋으로 들어가는 단어의 순서를 알기 위해 딕셔너리의 해당 단어의 index (순서)를 반환하기.
    
    # 첫 시도! 중복 있는 순열을 이용해서 전체 딕셔너리를 만들고자 함. ("AEIOU"에다가 빈자리를 뜻하는 "0")
    # "AE0IE" 이런식으로 공백값 "0"이 중간에 들어있지 않도록 하기가 까다로움.
    # 두번째 시도! 딕셔너리를 다섯자리 포문을 돌면서 일일이 만들음. -> 해결
    # 세번째 시도! 다섯자리 포문보다는 앞선 시도인 중복 있는 순열 방법 보완해서 만들기
    #           1) 중복있는 순열 (product) 로 1~5자리의 조합 만들고
    #           2) 포인트는 그냥 "0" 애초에 섞지 않고 딕셔너리를 다 만들고 나중에 빈자리에 채워주기
    
    '''
    # 두번째 시도!
    # 포문을 써서 다소 노가다?로 딕셔너리 생성
    
    # 입력값으로 받은 단어의 공백값을 전처리해줌 "I" -> "I0000"
    if len(word) < 5:
        for i in range(5-len(word)):
            word += '0'
    
    dictionary = []
    
    for fifth in '0AEIOU':
        for fourth in '0AEIOU':
            if (fourth == '0') & (fifth > "0"):
                continue
            for third in '0AEIOU':
                if (third == '0') & (fourth > "0"):
                    continue
                for second in '0AEIOU':
                    if (second == '0') & (third > "0"):
                        continue
                    for first in 'AEIOU':
                        wd = first + second + third + fourth + fifth 
                        dictionary.append(wd)        
                        # 포인트! 공백이 단어 사이에 들어가지 않도록 검사해야함.
                        # e.g.) "AI0I0" (X), "AII00" (O) 
                        # 이 안에서 검사해보기 이전꺼가 0이 아닌데 이후는 0일 수 없다
                        # e.g.) 5번째 자리가 '0'이면 4번째도 '0'일수 있지만 
                        #       5번째 자리가 'E'면 4,3,2,1 자리에 '0'이 올 수 없음 !!
                        
    # 딕셔너리를 정렬
    dictionary = sorted(dictionary)
    # 리스트 내부함수인 index() 메소드를 통해 인풋의 리스트 내 위치를 반환
    answer = dictionary.index(word) + 1
    return answer
    '''
    
    # 세번째 시도!
    # 순열로 풀고 싶다!! for 문 5개 싫다!
    
    alphabets = ['A', 'E', 'I', 'O', 'U']
    # 중복 순열 생성
    dictionary = []
    for n in range(1,6):
        dictionary += list(product(alphabets, repeat=n))
    dictionary = [''.join(permutes).strip() for permutes in dictionary]
    # 단어의 공백값을 전처리해줌 "I" -> "I0000"            
    dictionary = [ word + ("0"*(5-len(word))) if len(word) < 5 else word for word in dictionary]

    # 딕셔너리를 정렬 (딕셔너리의 크기: 3905)
    dictionary = sorted(dictionary)
    
    # 입력값으로 받은 단어의 공백값을 전처리해줌 "I" -> "I0000"
    if len(word) < 5:
            word += ('0' * (5-len(word)))
    
    # 리스트 내부함수인 index() 메소드를 통해 인풋의 리스트 내 위치를 반환
    answer = dictionary.index(word) + 1
    return answer

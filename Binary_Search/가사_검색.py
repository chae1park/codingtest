# 동빈북 p.370 이진 탐색 문제 30 가사 검색
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
# 해당 문제는 많은 풀이에서 Trie 구조를 이용하고 있다.
# Trie 구조란 주로 효율적인 문자열 검색에서 많이 쓰이는 것 같고, 자동 검색 추천에 활용된다고 한다.
# 단점은 문자열의 크기만큼의 공간이 필요하다는 것
# 시간복잡도: 생성시 O(M*L), 탐색시 시간복잡도: O(L)   (제일 긴 문자열의 길이를 L 총 문자열들의 수를 M)

# 아래는 내가 Trie 구조의 이해를 위해 참고한 페이지들이다.
# https://twpower.github.io/187-trie-concept-and-basic-problem
# https://velog.io/@hope1213/TRIE-%EA%B5%AC%EC%A1%B0

# 처음 떠오른 regex를 사용할 수 없는 이유: 검색키워드를 하나하나 regex 규칙으로 만들 수 없다. ('fro??' -> r'fro\w{2}')

# 본 문제에서 고려해야 할 것은 
# 1. 검색 키워드에 와일드카드가 접두사/접미사/전체로 이루어져 있는 경우를 나눠서 구현
# 2. 검색 키워드에 문자열 부분까지 탐색하다가 와일드카드가 시작할 때 탐색을 더이상 않고 와일드카드 수만으로 결과를 도출


def add(head, word):
    '''
    문자열을 Trie 구조로 저장하는 function이다.
    # head는 문자열을 저장할 완성될 딕셔너리
    # node는 head와 메모리를 공유하며 head안의 위치를 왔다갔다하며 자료를 insert하기 위함.    
    '''
        # 2. 검색 키워드에 문자열 부분까지 탐색하다가 와일드카드가 시작할 때 탐색을 더이상 않고 결과를 도출하게 하기 위해 문자 부분까지 속하는 모든 단어들의 갯수를 저장하려고 함
        
    # 1. head와 node의 메모리를 공유
    node = head
    # 2. 현재 단어의 갯수를 node를 지나면서 계속 저장
    word_len = len(word)
    # 3. 한 글자씩 for문을 돌며 insert하고자 함
    for c in word:
        # 4. 현재 상태에서 해당 문자가 처음 나올 때 
        if c not in node:
            # 4-1. 해당 문자를 key로 하는 새로운 공간(딕셔너리)을 만들어 줌. # {} 부분
            # 4-2. 해당 문자 위치까지 일치하는 단어들의 길이를 저장할 리스트 공간도 만듬 # 'len':[] 부분
            node[c] = {'len':[]}
        # 5. node의 위치를 방금 추가한 문자 안으로 옮김
        node = node[c]
        # 6. 해당 문자 위치까지 일치하는 본 단어의 길이를 저장
        node['len'].append(word_len)
    # 7.문자열의 끝을 'end'로 표시함 (해당 문제에서는 안해도 무관)
    node['end'] = True

def search(head, query):
    '''
    문자열이 Trie 구조로 저장된 딕셔너리에서 조건을 만족하는 단어 개수를 반환하는 function이다.
    # head는 문자열이 저장된 딕셔너리
    # node는 head와 메모리를 공유하며 head안의 위치를 왔다갔다하며 자료를 search하기 위함.
    # word는 찾을 단어 혹은 단어의 조건으로, 와일드카드 '?'가 1개 이상 포함되고 이것은 전체 문자열 뒤쪽에만 위치한다. 
    '''
    # 1. head와 node의 메모리를 공유
    node = head
    # 2. 단어의 길이 저장
    word_len = len(query)
    
    # 3. 한 글자씩 for문을 돎
    for i, c in enumerate(query):
        # 4. 와일드 카드가 나왔을 때 
        if c == '?':
        # 4-1. 더이상 탐색을 하지 않고 현재 위치까지 해당한 단어들의 길이가 모두 저장된 'len'안 리스트에서 글자수가 맞는 단어들의 갯수를 반환 
            return node['len'].count(word_len) 
        # 5. 해당 글자가 존재하지 않는 경우
        elif c not in node:
            # 5-1. 0 반환
            return 0
        # 6. 계속 탐색
        node = node[c]
    
def solution(words, queries):
    '''
    가사 단어들과 검색 키워드를 파라미터로 받아 해당 검색 키워드에 맞는 가사 단어의 개수를 반환하는 function이다.
    # words는 전체 가사 단어들이다.
    # queries는 검색 키워드이며 와일드카드 '?'가 1개 이상 포함되고 이것은 전체 문자열 뒤쪽 혹은 앞쪽에만 위치한다. 전체가 와일드카드로 이루어진 문자도 포함될 수 있다. 
    '''
    
    answer = []
    # 문자열을 Trie 형태로 저장할 딕셔너리 head, 같은 방법이지만 역방향 query를 위해 단어를 거꾸로 만들어 저장하는 딕셔너리 head_rev.
    head, head_rev = {}, {}
    # 전체가 와일드카드로 이루어진 경우를 대비해 가사의 길이만 담을 리스트
    all_qst = []
    
    # 1. 모든 가사를 딕셔너리에 Trie 구조 형태로 등록
    # 1-1. 정방형
    for word in words:
        add(head, word)
    # 1-2. 역방향
    for word in words:
        add(head_rev, word[::-1])
    # 1-3. 전체
    all_qst = [len(word) for word in words]
    
    # 2. 각 검색 키워드를 3가지에 따라 나눠서 검사
    for q in queries:
        q_len = len(q)
        # 2-1. 전체
        if q.count('?') == q_len: 
            answer.append(all_qst.count(q_len))
        # 2-2. 역방향
        elif q.startswith('?'): 
            answer.append(search(head_rev, q[::-1]))
        # 2-3. 정방향
        elif q.endswith('?'):
            answer.append(search(head, q))
        
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
output = [3, 2, 4, 1, 0, 5]
print('expected output', output)
print(solution(words, queries))

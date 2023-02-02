# 참고한 페이지들
# https://twpower.github.io/187-trie-concept-and-basic-problem
# https://velog.io/@hope1213/TRIE-%EA%B5%AC%EC%A1%B0


# 1. head는 문자열을 저장할 완성될 딕셔너리
head = {}

def add(word):
    # node는 head와 메모리를 공유하며 head안의 위치를 왔다갔다하며 자료를 insert하기 위함.
    
    # head와 node의 메모리를 공유
    node = head
    # 한 단어씩 for문을 돌며 insert하고자 함
    for w in word:
        # 현재 상태에서 해당 문자가 처음 나올 때 
        if w not in node:
            # 해당 문자를 key로 하는 새로운 공간(딕셔너리)을 만들어 줌.
            node[w]={}
        # node의 위치를 방금 추가한 문자 안으로 옮김
        node = node[w]
    # 문자열의 끝이 되었을때 제일 마지막 문자 안에서 'end' 표시를 해줌
    node['end'] = True

add('ab')
add('cd')
add('cda')
add('cb')

# print(head) 
# {'a': {'b': {'end': True}}, 'c': {'d': {'end': True, 'a': {'end': True}}, 'b': {'end': True}}}


def search(word):
    node = head
    for w in word:
        if w not in node:
            return False
        # 해당 문자 있다면 해당 문자 안으로 node 위치를 이동시킴
        node = node[w]
    # 해당 문자열이 딕셔너리에 존재하는 경우 node의 마지막 상태: {'end': True}
    if 'end' in node:
        return True
    # 존재하지 않는 경우 node의 마지막 상태는 딕셔너리 중간 어딘가에 멈춰있음
    else:
        return False

print(search('ab'))
print(search('ac'))

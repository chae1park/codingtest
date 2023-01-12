# # 동빈북 p.346 DFS/BFS 문제 18 괄호변환
# 아래 홈페이지에서 풀도록 권장되고 있음
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

p = "(()())()"
output = "(()())()"

# p = ")("
# output = "()"

# p = "()))((()"
# output = "()(())()"

print('expected output',output)


def isRightPT(p):
    '''
    올바른 괄호 문자열인지 검사하는 function
    '''
    stack_ls = []
    
    for word in p:
        if word == '(':
            stack_ls.append(word)
        elif word == ')':
            if stack_ls and stack_ls[-1] == '(':
                stack_ls.pop()
            else:
                return False
    return True

def splitPT(p):
    '''
    문자열을 두 균형잡힌 문자열 u, v로 분리하는 function
    '''
    cnt = 0
    
    if p[0] == '(':
        cnt += 1
    else:
        cnt -= 1 
    for i in range(1,len(p)): 
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1 
        if cnt == 0: 
            break
    return p[:i+1], p[i+1:]
    
def loop(p):
    answer = ''
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if len(p) == 0:
        return ''
    # 올바른 괄호 문자열인지 검사 후 맞다면 그대로 리턴
    if isRightPT(p):
        return p
    # 2. 문자열을 두 균형잡힌 괄호 문자열 u, v로 분리 (v는 빈 문자열이 될 수 있음)
    u, v = splitPT(p)

    if isRightPT(u): # 3-1. u가 올바른 괄호 문자열인 경우
        # 3-1. 문자열 v에 대해 1단계부터 다시 수행
        v_result = loop(v)
        # 3. 수행한 결과 문자열을 u에 이어 붙인 후 반환
        return u + v_result
    else: # 4. u가 올바른 괄호 문자열이 아닌 균형잡힌 괄호 문자열인 경우
        v_result = loop(v)
        # 4-1, 4-2. 빈 문자열에 '('를 붙이고 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어붙이기
        answer = '(' + v_result + ')'
        # 4-4. u의 첫번째와 마지막 문자를 제거
        u = u[1:-1]
        # 4-5. 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙이기   
        u = u.replace('(','-')
        u = u.replace(')','(')
        u = u.replace('-',')')
        answer += u
        return answer
    
def solution(p):
    answer = loop(p)
    return answer

print(solution(p))
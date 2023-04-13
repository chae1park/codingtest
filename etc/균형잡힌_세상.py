# input 부분
while True:
    s = input()
    if s == '.':
        break
    
    stack = [] 
    for ch in s: # 글자
        is_right = True
        if ch in ['(', '[']:
            stack.append(ch)

        if ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_right = False
                break
            
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_right = False
                break
             
    if not stack and is_right:
        print('yes')
    else:
        print('no')
        
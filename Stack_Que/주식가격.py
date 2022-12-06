def solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    print(answer)
    print(stack)
    '''
    for i in range(1, len(prices)): i는 현재 시간
        while stack:
            # 나 현재시간과 스택 비교
            compare = stack[-1]
            if prices[compare] > prices[i]: # 값이 떨어짐
                answer[i] = i - compare # 비교대상과 현재의 인덱스 차이를 답 리스트에 저장
    
    '''
    for i in range(1, len(prices)):
        print('i',i)
        while stack:
            index = stack[-1]
            print('index',index)
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                print('prices[index] > prices[i]',prices[index],'>',prices[i])
                answer[index] = i - index
                print('answer[index] =',i - index)
                print('popped', stack[-1])
                stack.pop()
                print('left stack',stack)
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
        print('stack appended',stack[-1])
        
    return answer
    
    
                
    # input: [1, 2, 3, 1, 2]
    # output: [4, 2, 1, 1, 0]
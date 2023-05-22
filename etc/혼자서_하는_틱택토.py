# https://school.programmers.co.kr/learn/courses/30/lessons/160585#
def solution(board):
    answer = 0
    # 경우의 수 문제!
    # 1) 갯수만 봣을때는 X가 O보다 많거나, O-X > 1
    # 2) 이미 하나가 빙고인데 또 빙고인경우  
    # 3) Obing 있을때 X갯수 똑같으면 안됨
    # 4) Xbing 있을때 O,X갯수 똑같아야 됨
    
# OOO
# .X.
# XX. -> Obing 있을때 X갯수 똑같으면 안됨

# XXX
# .O.
# OO. -> 이건 괜찮음
    
    # 1. 갯수세기
    Os = 0
    Xs = 0
    for b in board:
        Os += b.count('O')
        Xs += b.count('X')
    # 1) X가 O보다 많거나, O-X > 1
    if (Xs > Os) or (Os - Xs > 1):
        return answer
    # 2. 빙고 여부
    Obing, Xbing = 0, 0
    # 2-1. 가로로 빙고 여부
    for i in range(3):
        Ocnt, Xcnt = 0, 0
        for j in range(3):
            if board[i][j] == 'O':
                Ocnt += 1
            elif board[i][j] == 'X':
                Xcnt += 1
        if Ocnt == 3:
            Obing += 1
        elif Xcnt == 3:
            Xbing += 1
    # 2-1. 세로로 빙고 여부
    for j in range(3):
        Ocnt, Xcnt = 0, 0
        for i in range(3):
            if board[i][j] == 'O':
                Ocnt += 1
            elif board[i][j] == 'X':
                Xcnt += 1
        if Ocnt == 3:
            Obing += 1
        elif Xcnt == 3:
            Xbing += 1
    # 2-3. 오른쪽 대각선 빙고 여부
    Ocnt, Xcnt = 0, 0
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == 'O':
            Obing += 1
        elif board[1][1] == 'X':
            Xbing += 1
    # 2-3. 왼쪽 대각선 빙고 여부
    if board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == 'O':
            Obing += 1
        elif board[1][1] == 'X':
            Xbing += 1
            
    # 2) 이미 하나가 빙고인데 또 빙고인경우  
    if Obing + Xbing > 2:
        return answer
    # 3) Obing 있을때 X갯수 똑같으면 안됨
    if Obing:
        if Os - Xs != 1:
            return answer
    # 4) Xbing 있을때 O,X갯수 똑같아야 됨
    if Xbing:
        if Os != Xs:
            return answer
    # 나머지 경우 정상 출력
    answer = 1
    return answer
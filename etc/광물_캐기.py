# https://school.programmers.co.kr/learn/courses/30/lessons/172927

# 한번에 구현해서 맞춘 문제라서 다른사람들의 풀이방법은 모르지만
# 수 범위가 크지 않기에 딕셔너리를 만들고 광물 하나씩 캐었더니 통과할 수 있었다.

def mining(status, mine_type):
    # 광물 캐고, 피로도 계산하는 함수
    
    # status: 이번 세트에서 캐야할 광물 현황
    # mine_type: 해당 세트를 캘 곡괭이 (고정)
    
    ans = 0 # 피로도
    cnt = 5 # 남은 광물 수
    mineral_type = 0 # 광물 종류 인덱스
    
    # 광물 다 캐거나 곡괭이가 없을때까지
    while (cnt > 0) and (mineral_type <= 2):
        while status[mineral_type] != 0: # 해당 자리에 있는 캘 광물이 남아있을 때
            if mine_type == mineral_type: # 동급의 곡괭이와 광물이면 공통적으로 1 소모
                # 광물 캠
                status[mineral_type] -= 1
                ans += 1
                cnt -= 1
            elif mine_type == mineral_type + 1: # iron == dia+1 (한단계 차이면 5 소모)
                # 광물 캠
                status[mineral_type] -= 1
                ans += 5
                cnt -= 1

            elif mine_type == mineral_type + 2: # rock == dia+2 (두단계 차이면 25 소모)
                # 광물 캠
                status[mineral_type] -= 1
                ans += 25
                cnt -= 1
            else: # dia mine --> rock (상위 곡괭이로 하위 곡괭이를 캐면 전부 1 소모)
                # 광물 캠
                status[mineral_type] -= 1
                ans += 1
                cnt -= 1
        # 해당 자리의 광물을 다 캤으면 다음 광물 종류로 넘어감
        mineral_type += 1
    
    # 피로도 반환
    return ans
        
        
def solution(picks, minerals):
    answer = 0
    n = len(minerals)
    # 1. 값이 많이 나가는 광석 5개 셋트 순으로 정렬하기 위해 딕셔너리 초기화
    costs = {i:0 for i in range(n//5 + 1)} 
    for i in range(0, n):
        h = i // 5
        if minerals[i] == 'diamond':
            costs[h] += 100
        elif minerals[i] == 'iron':
            costs[h] += 10
        else: 
            costs[h] += 1
            
    # 2. 가진 곡괭이 수로 채굴할 수 없는 광물 가지치기
    n_mines = sum(picks) # 곡괭이 수 2개일 경우 10개만 가능함
    order = list(costs.items())[:n_mines] # 남은 광석 세트가 3세트면 2세트만 가능하고 나머지 버림
    
    # 3. 딕셔너리를 광물값어치 높은 순으로 정렬
    order = sorted(order, key=lambda x: -x[1])
    # 4. 편한 처리를 위해 정수를 문자열로 변경 (41 -> '041', 331 -> '331')
    order = [(idx, str(cost).zfill(3)) for idx, cost in order]
    
    # 곡괭이 인덱스 (0: 다이아, 1: 철, 2:돌)
    mine_type = 0       
    # 광물 인덱스 (0: 다이아, 1: 철, 2:돌)
    mineral_type = 0
    
    # 항상 처리할 광물 세트보다 곡괭이가 넉넉하므로 광물 세트를 기준으로 남김없이 반복문
    for idx, cost in order: # 세트번호, 해당 세트의 광물갯수(문자열 형태)
        # status에 광물 개수 현황을 저장 (다이아:3개, 철:1개, 돌:1개)
        status = {i: int(cost[i]) for i in range(3)}
        # 제일 비싼 곡괭이가 남아있다면 그 곡괭이로 픽스함
        if picks[mine_type] >= 1:
            # 곡괭이 소비
            picks[mine_type] -= 1
            # 광물을 캐고, 피로도 계산
            answer += mining(status, mine_type)
            
        # 제일 비싼 곡괭이가 없다면    
        else:
            # 그 다음 비싼 곡괭이로 픽스함  
            while picks[mine_type] < 1:
                mine_type += 1
            # 곡괭이 소비
            picks[mine_type] -= 1
            # 광물을 캐고, 피로도 계산         
            answer += mining(status, mine_type)
    
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    # 가능한 모든 던전 탐험 루트를 탐색하기 위해 순열 사용
    # 완전 탐색의 근거 : 던전의 전체 갯수가 작은 8 이하이므로 최대 40,320회만 돌면 됨
    answer = -1
    candid_dungeon = list(permutations(dungeons))
    
    for candid in candid_dungeon:
        # 해당 조합에서의 돌 수 있는 던전 갯수 
        num_exp_dun = 0
        # 해당 조합에서의 피로도 계산
        left_k = k
        
        # 모든 조합에서의 던전을 순서대로 루프
        for dun in candid:
            # 현재 피로도를 가지고 남은 던전을 탐색할 수 있는지 검사 후 던전 탐색 
            if (left_k >= dun[0]) :
                left_k -= dun[1]
                num_exp_dun += 1
            # 더이상 남은 피로도를 가지고 남은 던전을 탐색할 수 없을 때 탐색 중단
            else:
                break
                
        # 정답의 순서는 필요없고 정답일 때의 최댓값만 필요로 하기 때문에 최댓값만 계속 갖고 있기
        answer = max(answer, num_exp_dun)
        
    return answer

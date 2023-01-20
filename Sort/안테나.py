# 동빈북 p.360 정렬 문제 24 안테나
# https://www.acmicpc.net/problem/18310

# 모든 집까지의 거리의 총 합이 최소가 되도록 하는 집을 선택해서 반환
# 이 말은 즉 중간값을 찾기
# 짝수일 경우, 중간값이 두개인데 거리가 최소로 같다면 그 중 수가 작은 것을 반환

import numpy as np
N = 4
houses = [5,1,7,9]
houses = [1, 3, 3, 3, 6, 6, 7, 9]
output = 5
print('expected output',output)

houses.sort()
print(houses[len(houses)//2 - 1])

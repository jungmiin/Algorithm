# 치킨 배달 23/3/22 18:00 - 18:30 

# 맵 돌면서 치킨집 좌표 저장
# 해당 좌표 리스트를 기준으로 m개만큼 정하는 조합 리스트 만들기
# 해당 조합 리스트 돌면서 최솟값 갱신
# 조합 리스트 안에서도 최소 거리 찾아야함... -> 어떻게? 

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []
distance = 20000
for i, row in enumerate(city):
    for j, element in enumerate(row):
        if element == 2:
            chicken.append((i, j))
        elif element == 1:
            home.append((i, j))

combi_chicken = list(combinations(chicken, M))

for combi in combi_chicken:
    tmp_distance = 0
    for hx, hy in home:
        tmp = 100
        for cx, cy in combi:
            tmp = min(tmp, abs(cx-hx)+abs(cy-hy))
        tmp_distance += tmp
    distance = min(distance, tmp_distance)

print(distance)
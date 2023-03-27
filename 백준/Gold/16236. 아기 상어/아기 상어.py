# 아기상어 2023/3/22 21:00

# 거리가 가까운 물고기 -> 가장 위에 있는 물고기 -> 가장 왼쪽에 있는 물고기
# 총 몇 초동안 물고기 잡아먹을 수 있는가
# 가장 처음 아기 상어 크기 2
# 크기가 큰 물고기 지나갈 수 X 크기가 같은 물고기 지나갈수 O 크기가 작은 물고기 먹을 수 O

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c, size):
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((r, c))
    fish = []
    while queue:
        qr, qc = queue.popleft()
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i] 
            if not (nr == r and nc == c) and 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 :
                if graph[nr][nc] <= size :
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[qr][qc] + 1
                    if graph[nr][nc] < size and graph[nr][nc] != 0 :
                        fish.append((nr, nc, visited[nr][nc]))
    return sorted(fish, key = lambda x : (-x[2], -x[0], -x[1]))

shark_r = -1
shark_c = -1
size = 2

for r, row in enumerate(graph):
    for c, column in enumerate(row):
        if column == 9:
            shark_r = r
            shark_c = c

second = 0
cnt = 0

while True:
    fish = bfs(shark_r, shark_c, size)
    if fish :
        r, c, d = fish.pop()
        second += d
        graph[shark_r][shark_c], graph[r][c] = 0, 0
        shark_r, shark_c = r, c
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
    else : 
        break

print(second)






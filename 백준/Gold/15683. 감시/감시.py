# 감시 

cctv = { 1: [[(1,0)], [(-1, 0)], [(0, 1)], [(0, -1)]],
        2: [[(1,0), (-1, 0)], [(0, 1), (0, -1)]],
        3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        5: [[(1, 0), (-1, 0), (0, 1), (0, -1)]]
        }

import sys
import itertools
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

blind_spot = 64

cctv_pos = []

for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            cctv_pos.append((i, j, graph[i][j]))

all_list = []
for pos in cctv_pos:
    all_list.append(cctv[pos[2]])
all_con = list(itertools.product(*all_list))

for i, con in enumerate(all_con):
    # print(i)
    tmp = deepcopy(graph)
    cnt = 0
    for i, coord in enumerate(con):
        # print(cctv_pos[i],":",coord)
        for c in coord:
            nx, ny = cctv_pos[i][0], cctv_pos[i][1]
            # print(c)
            nx += c[0]
            ny += c[1]
            while True:
                if 0<=nx<N and 0<=ny<M and tmp[nx][ny] != 6:
                    # print("move!!", nx, ny)
                    tmp[nx][ny] = '#'
                    nx += c[0]
                    ny += c[1]
                else:
                    # print("break!!", nx, ny)
                    break
                
    for j in range(N):
        # print(''.join(map(str, tmp[j])))
        for k in range(M):
            if tmp[j][k] == 0:
                cnt += 1
    blind_spot=min(cnt, blind_spot)

print(blind_spot)

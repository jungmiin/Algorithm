# 로봇청소기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dc = [0, 1, 0, -1] 
dr = [-1, 0, 1, 0]

clean_area = 0

def bfs() :
    global clean_area
    queue = deque()
    queue.append((R, C, D))
    while queue:
        # print(queue)
        r, c, d = queue.popleft()
        if graph[r][c] == 0:
            graph[r][c] = 2
            clean_area += 1
        near = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                near = True
        if near:
            for i in range(1, 5):
                nd = (d-i)%4
                nr = r + dr[nd]
                nc = c + dc[nd]
                if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                    queue.append((nr, nc, nd))
                    break
        else :
            br = r - dr[d]
            bc = c - dc[d]
            if 0 <= br < N and 0 <= bc < M and graph[br][bc] == 2:
                queue.append((br, bc, d))
            else : 
                break


bfs()

# for i in range(N):
#     print()
#     for j in range(M):
#         print(graph[i][j], end=' ')

print(clean_area)
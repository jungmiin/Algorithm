# 미세먼지 안녕!

import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

# 동북서남
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
cleaner = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            cleaner.append((i, j))

for _ in range(T):
    # 미세먼지 확산
    save_graph = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                d = graph[r][c]
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                        save_graph[nr][nc] += d//5
                        graph[r][c] = max(0, graph[r][c] - d//5)
    for r in range(R):
        for c in range(C):
            graph[r][c] += save_graph[r][c]
        
    # for r, c in dust:
    #     d = graph[r][c]
    #     if d== 0:
    #         continue
    #     for i in range(4):
    #         nr = r + dr[i]
    #         nc = c + dc[i]
    #         if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
    #             graph[nr][nc] += d//5
    #             graph[r][c] = max(0, graph[r][c] - d//5)

    # print("확산")
    # for j in range(R):
    #     print()
    #     for k in range(C):
    #         print(graph[j][k], end=' ')
    # print()
    # 공기청정기 작동
    # 위칸 -> 반시계
    r, c = cleaner[0]
    prev_coord = 0
    for i in range(4):
        while True:
            nr = r + dr[i] 
            nc = c + dc[i] 
            if 0 <= nr < R and 0 <= nc < C:
                if graph[nr][nc] == -1:
                    break
                next_coord = graph[nr][nc]
                graph[nr][nc] = prev_coord
                prev_coord = next_coord
                r, c = nr, nc
            else :
                break
    # 아래칸 -> 시계
    r, c = cleaner[1]
    prev_coord = 0
    for i in range(0, -4, -1):
        while True:
            nr = r + dr[i] 
            nc = c + dc[i] 
            if 0 <= nr < R and 0 <= nc < C:
                if graph[nr][nc] == -1:
                    break
                next_coord = graph[nr][nc]
                graph[nr][nc] = prev_coord
                prev_coord = next_coord
                r, c = nr, nc
            else :
                break
    # print("공기청정기")
    # for j in range(R):
    #     print()
    #     for k in range(C):
    #         print(graph[j][k], end=' ')

answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)
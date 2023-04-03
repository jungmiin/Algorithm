#  드래곤 커브

import sys

input = sys.stdin.readline

N = int(input().rstrip())
curves = [list(map(int, input().split())) for _ in range(N)]
graph = [[0]*101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for curve in curves:
    x, y, d, g = curve
    graph[x][y] = 1
    move = [d]
    for i in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1)% 4)
        move.extend(tmp)
    for m in move:
        mx = x + dx[m]
        my = y + dy[m]
        graph[mx][my] = 1
        x, y = mx, my

answer = 0 
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            answer += 1

print(answer)
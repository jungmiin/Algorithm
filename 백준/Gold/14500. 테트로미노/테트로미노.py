# 테트로미노 23/3/23 18:53 -

# 테트로미노의 모든 경우를 (대칭, 회전한 경우 다) 저장해놓고 map 에 대입해보고 최대값 저장?

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0

def bfs(r, c):
    global answer
    queue = deque()
    queue.append((r, c, [(r, c)]))
    while queue:
        qr, qc, tmp = queue.popleft()
        if len(tmp) > 4:
            continue
        elif len(tmp) == 4:
            sum = 0
            for tr, tc in tmp:
                sum += paper[tr][tc]
            answer = max(answer, sum)
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in tmp:
                queue.append((nr, nc, tmp+[(nr, nc)]))

# ㅓㅏㅗㅜ
def other_case(r, c):
    global answer
    shapes = [((0, -1), (-1, 0), (1, 0)), ((0, 1), (-1, 0), (1, 0)), ((-1, 0), (0, -1), (0, 1)), ((1, 0), (0, -1), (0, 1))]
    for shape in shapes:
        if 0 <= r+shape[0][0] < N and 0 <= r+shape[1][0] < N and 0 <= r+shape[2][0] < N and 0 <= c+shape[0][1] < M and 0 <= c+shape[1][1] < M and 0 <= c+shape[2][1] < M :
            sum = paper[r][c]
            for i in range(3):
                sum += paper[r+shape[i][0]][c+shape[i][1]]
            answer = max(answer, sum)

for i in range(N):
    for j in range(M):
        bfs(i, j)

for i in range(N):
    for j in range(M):
        other_case(i, j)

print(answer)


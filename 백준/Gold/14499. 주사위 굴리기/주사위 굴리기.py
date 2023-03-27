# 주사위 굴리기 23/3/27 10:39-
# 주사위를 굴린다
# -> 만약 이동한 지도의 칸의 숫자가 0이면 
#     주사위의 숫자가 지도의 숫자로 복사
# -> 만약 이동한 지도의 칸의 숫자가 0이 아니면
#     지도의 숫자가 주사위 바닥면의 숫자로 복사 
#     이후 지도의 숫자는 0이 됨

# 명령 만큼 반복
#     이동 구현 후
#     주사위 바닥면과 지도 숫자 확인
#     변경

import sys
from collections import deque

input = sys.stdin.readline

N, M, X, Y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, -1, 1]
nx, ny = X, Y
dice = [0, 0, 0, 0, 0, 0]

def roll(direction):
    global dice
    a, b, c, d, e, f = dice
    if direction == 1: #동
        dice = [d, b, a, f, e, c]
    elif direction == 2: #서
        dice = [c, b, f, a, e, d]
    elif direction == 3: #북
        dice = [e, a, c, d, f, b]
    elif direction == 4: #남
        dice = [b, f, c, d, a, e]
        

for direction in command:
    nx+=dx[direction]
    ny+=dy[direction]
    if 0 <= nx < N and 0 <= ny < M:
        roll(direction)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[-1]
        else:
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice[0])
    else :
        nx-=dx[direction]
        ny-=dy[direction]

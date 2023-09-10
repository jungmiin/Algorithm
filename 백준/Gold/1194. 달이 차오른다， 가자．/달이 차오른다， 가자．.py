import sys
from collections import deque
input = sys.stdin.readline

# 7, -1, 55, 3, 6, 19, 12, -1

TEST_CASE = 1 # 테스트 케이스 수
INF = int(1e9)
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution():
    N, M = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(N)]
    sr, sc = 0, 0
    for i in range(N):
        for j in range(M):
            if maze[i][j] == '0':
                sr, sc = i, j
    def bfs(r, c):
        visited = [[[False]*(1<<6) for _ in range(M)] for _ in range(N)]
        queue = deque()
        queue.append((r, c, 0, 0)) # r, c, cnt, 열쇠 가진 것들
        visited[r][c][0] = True
        while queue:
            r, c, cnt, key = queue.popleft()
            if maze[r][c] == '1':
                return cnt
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if not maze[nr][nc] == '#' and not visited[nr][nc][key]:
                        next_key = key
                        if 'a' <= maze[nr][nc] <= 'f':
                            next_key |= 1<<(ord(maze[nr][nc])-ord('a'))
                        if (not 'A' <= maze[nr][nc] <= 'F') or (key&1<<(ord(maze[nr][nc])-ord('A'))):
                            visited[nr][nc][next_key] = True
                            queue.append((nr, nc, cnt+1, next_key))
        return -1
    print(bfs(sr, sc))
for _ in range(TEST_CASE):
    solution()
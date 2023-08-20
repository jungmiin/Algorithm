import sys
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def dfs(r, c):
    if r == M-1 and c == N-1: return 1 
    if dp[r][c] != -1:
        return dp[r][c]
    result = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] < graph[r][c]:
            result += dfs(nr, nc)
    dp[r][c] = result
    return dp[r][c]

print(dfs(0, 0))

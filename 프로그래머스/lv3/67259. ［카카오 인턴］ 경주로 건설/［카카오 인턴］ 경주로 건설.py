from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# right = 0 left = 2 down = 1 up = 3
INF = int(1e9)

def solution(board):
    N = len(board)
    dp = [[INF] * N for _ in range(N)]
    def dfs(row, col, direction, cost):
        if dp[row][col] >= cost: dp[row][col] = cost 
        else: return False
        if row == col == N-1: return
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                next_cost = 100
                if direction != -1 and (direction + i) % 2 == 1:
                    next_cost += 500
                board[nr][nc] = -1
                dfs(nr, nc, i, cost + next_cost)
                board[nr][nc] = 0
        return False
    dfs(0, 0, -1, 0)
    return dp[N-1][N-1]
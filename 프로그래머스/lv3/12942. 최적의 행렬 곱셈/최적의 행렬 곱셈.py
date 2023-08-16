def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[int(1e9)] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for middle in range(1, N):
        for first in range(N):
            last = first + middle
            if last < N:
                for i in range(first, last):
                    dp[first][last] = min(dp[first][last], dp[first][i] + dp[i+1][last] + (matrix_sizes[first][0] * matrix_sizes[i][1] * matrix_sizes[last][1]))
    return dp[0][-1]
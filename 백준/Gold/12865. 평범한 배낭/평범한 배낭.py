import sys

N, K = map(int, sys.stdin.readline().split())
M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, K+1):
    [weight, value] = M[i-1]
    if j < weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
      
print(dp[N][K])
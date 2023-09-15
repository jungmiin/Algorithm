import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
INF = int(1e9)

def solution():
    result = INF
    N = int(input().rstrip())
    costs = [list(map(int, input().split())) for _ in range(N)]
    for i in range(3):
        dp = [[INF]*3 for _ in range(N)]
        dp[0][i] = costs[0][i]
        for j in range(1, N):
            dp[j][0] = costs[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = costs[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = costs[j][2] + min(dp[j-1][0], dp[j-1][1])
        for j in range(3):
            if i != j:
                result = min(result, dp[-1][j])
    print(result)

for _ in range(TEST_CASE):
    solution()
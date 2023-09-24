import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
INF = int(1e9)

def solution():
    N = int(input().rstrip())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 if n == m else INF for m in range(N)] for n in range(N)]
    for interval in range(1, N):
        for start in range(N-interval):
            for i in range(start, start+interval):
                dp[start][start+interval] = min(dp[start][start+interval], 
                                                dp[start][i] + dp[i+1][start+interval] + matrix[start][0]*matrix[i][1]*matrix[start+interval][1])
    print(dp[0][-1])

for _ in range(TEST_CASE):
    solution()
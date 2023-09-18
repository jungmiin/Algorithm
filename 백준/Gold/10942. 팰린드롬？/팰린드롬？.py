import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N = int(input().rstrip())
    numbers = [0]+list(map(int, input().split()))
    M = int(input().rstrip())
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N, 0, -1):
        for j in range(i, N+1):
            if i == j: dp[i][j] = 1
            elif j-i == 1: dp[i][j] = 1 if numbers[i] == numbers[j] else 0
            else:
                if dp[i+1][j-1] == 1 and numbers[i] == numbers[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
    for _ in range(M):
        start, end = map(int, input().split())
        print(dp[start][end])
for _ in range(TEST_CASE):
    solution()
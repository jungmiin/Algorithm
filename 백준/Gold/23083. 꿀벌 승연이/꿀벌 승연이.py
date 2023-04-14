import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def main():
    def k():
        K = int(input().rstrip())
        for _ in range(K):
            i, j = map(int, input().split())
            dp[i][j] = 0

    def find(i, j):
        if dp[i][j] != -1: return dp[i][j]
        val = find(i-1, j)+find(i, j-1)
        val += find(i-1, j-1) if j%2 else find(i+1, j-1)
        dp[i][j] = int(val%(1e9+7))
        return dp[i][j]

    N, M = map(int, input().split())
    dp = [[-1] * (M+1) for _ in range(N+2)]
    dp[1][1] = 1
    for i in range(N+2):
        dp[i][0] = 0
    for i in range(M+1):
        dp[0][i] = 0
        dp[N+1][i] = 0
    k()
    find(N, M)

    print(dp[N][M])

main()
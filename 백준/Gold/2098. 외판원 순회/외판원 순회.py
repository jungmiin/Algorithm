import sys
from collections import defaultdict
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
INF = int(1e8)

def solution():
    N = int(input().rstrip())
    W = [list(map(int, input().split())) for _ in range(N)]
    dp = defaultdict(lambda:INF)
    def dfs(i, visited):
        if visited == (1<<N)-1:
            if W[i][0]:
                return W[i][0]
            else:
                return INF
        if (i, visited) in dp:
            return dp[(i, visited)]
        for j in range(1, N):
            if W[i][j] == 0:
                continue
            elif visited & (1<<j):
                continue
            dp[(i, visited)] = min(dp[(i, visited)], dfs(j, visited|(1<<j))+W[i][j])
        return dp[(i, visited)]
    print(dfs(0, 1))

for _ in range(TEST_CASE):
    solution()
import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N, M = map(int, input().split())
    memories = [0] + list(map(int, input().split())) 
    costs = [0] + list(map(int, input().split())) 
    dp = [[0 for _ in range(sum(costs)+1)] for _ in range(N+1)] 
    answer = sum(costs)
    for i in range(1, N+1):
        memory = memories[i]
        cost = costs[i]
        for j in range(1, sum(costs) + 1):
            if j < cost: 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(memory + dp[i-1][j-cost], dp[i-1][j])
            if dp[i][j] >= M: 
                answer = min(answer, j)
    if M != 0:
        print(answer)
    else:
        print(0)
for _ in range(TEST_CASE):
    solution()
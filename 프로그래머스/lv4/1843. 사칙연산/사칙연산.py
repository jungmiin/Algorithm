INF = int(1e9)
def solution(arr):
    answer = -1
    number, operator = [int(arr[i]) for i in range(0, len(arr), 2)], [arr[i] for i in range(1, len(arr), 2)]
    N = len(number)
    min_dp, max_dp = [[INF] * N for _ in range(N)], [[-INF] * N for _ in range(N)]
    for scope in range(N):
        for start in range(N-scope):
            end = start + scope
            if scope == 0:
                min_dp[start][start] = max_dp[start][start] = number[start]
            else:
                for mid in range(start, end):
                    if operator[mid] == '+':
                        max_dp[start][end] = max(max_dp[start][end], max_dp[start][mid]+max_dp[mid+1][end])
                        min_dp[start][end] = min(min_dp[start][end], min_dp[start][mid]+min_dp[mid+1][end])
                    elif operator[mid] == '-':
                        max_dp[start][end] = max(max_dp[start][end], max_dp[start][mid]-min_dp[mid+1][end])
                        min_dp[start][end] = min(min_dp[start][end], min_dp[start][mid]-min_dp[mid+1][end])
    # for i in max_dp:
    #     print(i)
    return max_dp[0][N-1]
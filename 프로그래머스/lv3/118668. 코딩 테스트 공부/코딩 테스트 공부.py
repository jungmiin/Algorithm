INF = int(1e9)

def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i + 1 <= max_alp:
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j] + 1, dp[i][j+1])
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    # print(dp)
    return dp[-1][-1]
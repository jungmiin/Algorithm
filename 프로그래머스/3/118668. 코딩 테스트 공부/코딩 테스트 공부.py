INF = int(1000)
def solution(alp, cop, problems): # 초기 알고력, 초기 코딩력, 문제 [필요한 알고력, 필요한 코딩력, 증가 알고력, 증가 코딩력, 시간]
    answer = INF
    max_alp, max_cop = alp, cop
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    alp, cop = min(max_alp, alp), min(max_cop, cop)
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1, dp[i][j-1]+1)
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_req <= i and cop_req <= j:
                    ni, nj = min(max_alp, i+alp_rwd), min(max_cop, j+cop_rwd)
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j]+cost)
        # print(*dp, sep="\n")
    # for i in range(max_alp, MAX_RANGE+1):
    #     for j in range(max_cop, MAX_RANGE+1):
    #         answer = min(answer, dp[i][j])
    return dp[max_alp][max_cop]

def solution(sales, links):
    answer = 0
    N = len(sales) # 회사원 수
    sales = [-1] + sales
    dp = [[0, 1] for _ in range(N+1)]
    adj = [[] for _ in range(N+1)] # 팀원 - 팀장 관계 인접 리스트로 저장
    for leader, member in links:
        adj[leader].append(member)
    def dfs(leader):
        if len(adj[leader]) == 0:
            dp[leader][0], dp[leader][1] = 0, sales[leader]
            return
        gap = int(1e9)
        dp[leader][1] = sales[leader]
        for member in adj[leader]:
            dfs(member)
            dp[leader][1] += min(dp[member][0], dp[member][1]) 
            gap = min(gap, dp[member][1] - dp[member][0])
        if gap < 0: 
            gap = 0 
        dp[leader][0] = dp[leader][1] + gap - sales[leader]
    dfs(1)
    return min(dp[1])
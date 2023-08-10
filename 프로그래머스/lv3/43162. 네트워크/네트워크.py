from collections import defaultdict
def solution(n, computers):
    network = 0
    visited = [False] * n
    adj = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if not i == j and computers[i][j] == 1:
                adj[i].append(j)
                
    def dfs(computer):
        # print("dfs:", computer)
        for com in adj[computer]:
            if not visited[com]:
                # print("not visited:", com)
                visited[com] = True
                dfs(com)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            network += 1

    return network

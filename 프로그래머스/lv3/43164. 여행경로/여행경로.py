import heapq
from collections import defaultdict

def dfs(result, N, adj, a1):
    result.append(a1)
    if len(result) == N + 1:
        return True
    
    if a1 not in adj:
        result.pop()
        return False
    
    for _ in range(len(adj[a1])):
        a2 = adj[a1].pop()
        if dfs(result, N, adj, a2):
            return True
        adj[a1].insert(0, a2)
        
    result.pop()
    return False

def solution(tickets):
    answer = []
    result = []
    adj = defaultdict(list)
    
    for ticket in tickets:
        a1, a2 = ticket
        adj[a1].append(a2)
        
    for a in adj.keys():
        adj[a].sort(reverse=True)
        
    dfs(result, len(tickets), adj, "ICN")
    return result

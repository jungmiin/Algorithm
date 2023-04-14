import heapq
from collections import defaultdict
result = []

def dfs(adj, a1):
    global result
    print(adj)
    result.append(a1)
    while adj[a1]:
        a2 = heapq.heappop(adj[a1])
        dfs(adj,a2)
    return result

def solution(tickets):
    answer = []
    adj = defaultdict(list)
    for ticket in tickets:
        a1, a2 = ticket
        heapq.heappush(adj[a1], a2)

    return dfs(adj, "ICN")

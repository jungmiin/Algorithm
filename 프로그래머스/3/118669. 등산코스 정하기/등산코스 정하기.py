from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    ans_summit, ans_intensity = -1, int(1e9)
    g, s = set(gates), set(summits)
    is_gate = [i in g for i in range(n+1)]
    is_summit = [i in s for i in range(n+1)]
    
    # 인접리스트 초기화
    adj = defaultdict(list)
    for i, j, w in paths:
        adj[i].append((j, w))
        adj[j].append((i, w))
    
    # 탐색
    queue = []
    
    for gate in gates:
        heapq.heappush(queue, (0, gate))
        
    dp = [int(1e9)] * (n+1)
    for gate in gates:
        dp[gate] = 0
    # print(adj)
    while queue:
        intensity, node = heapq.heappop(queue) # intensity, node
        if intensity > dp[node] or is_summit[node]:
            continue
        for next_node, next_intensity in adj[node]:
            next_intensity = max(dp[node], next_intensity)
            if dp[next_node] > next_intensity:
                dp[next_node] = next_intensity
                heapq.heappush(queue, (next_intensity, next_node))
    # print(dp)     
    answer = [0, int(1e9)]
    for summit in sorted(summits):
        if dp[summit] < answer[1]:
            answer[0], answer[1] = summit, dp[summit]
    return answer
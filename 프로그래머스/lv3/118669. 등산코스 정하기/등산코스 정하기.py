import heapq
from collections import defaultdict, deque
from copy import deepcopy

def bfs(n, graph, summits_set, summits, gates):
    min_intensity = 10000001
    min_summit = 50001
    visited = [10000001]*(n+1)
    hq = []
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        visited[gate] = 0

    while hq:
        intensity, node = heapq.heappop(hq)
        if node in summits_set or intensity > visited[node]:
            continue
        for weight, next_node in graph[node]:
            new_intensity = max(intensity, weight)
            if new_intensity < visited[next_node]:
                visited[next_node] = new_intensity
                heapq.heappush(hq, (new_intensity, next_node))
                
    for summit in summits:
        if visited[summit] < min_intensity:
            min_summit = summit
            min_intensity = visited[summit]
            
    return [min_summit, min_intensity]
            

def solution(n, paths, gates, summits):
    answer = []
    summits_dict = {n: False for n in range(n+1)}
    summits.sort()
    summits_set = set(summits)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    for summit in summits:
        summits_dict[summit] = True

    return bfs(n, graph, summits_set, summits, gates)
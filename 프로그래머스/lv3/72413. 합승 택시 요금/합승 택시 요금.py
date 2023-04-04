# 지점 개수 n 출발지점 s a 도착지점 a b 도착지점 b 지점 사이의 예상 요금 fares
# 인접리스트 작성, 시작 위치에서 각 지점 도착 요금 출력, 합승 안했을 때 요금 저장 이후 min으로 비교
# 이후 그 지점 리스트 돌면서 (도착 요금 작은거 순서대로) 합승했을때 a b위치 도착요금 계산, min으로 비교하며 업데이트

import heapq 
INF = int(1e9)

def dijkstra(adj, start, n):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_node, next_cost in adj[node]:
            if next_cost + cost < distance[next_node]:
                distance[next_node] = next_cost + cost
                heapq.heappush(queue, (distance[next_node], next_node))
    return distance
            

def solution(n, s, a, b, fares):
    answer = 0
    adj = [[] for _ in range(n+1)]
    cost = 0
    for start, end, fare in fares:
        adj[start].append((end, fare))
        adj[end].append((start, fare))
    distance = dijkstra(adj, s, n)
    cost = distance[a] + distance[b]
    for i in range(1,n+1):
        if i == s:
            continue
        distance_tmp = dijkstra(adj, i, n)
        cost = min(cost, distance[i]+distance_tmp[a]+distance_tmp[b])
    
    return cost
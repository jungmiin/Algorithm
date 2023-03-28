#  파티
#  다익스트라 두번 돌려서 계산하면 된단 뜻인가?

import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

N, M, X = map(int, input().split())
adj = [[] for _ in range(N+1)]


for i in range(M):
    start, end, time = map(int, input().split())
    adj[start].append((time, end))

def dijkstra(start):
    distance = [INF] * (N + 1)
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        cost, node = heapq.heappop(queue)

        if distance[node] < cost:
            continue

        for next_cost, next_node in adj[node]:
            if next_cost + cost < distance[next_node] :
                distance[next_node] = next_cost + cost
                heapq.heappush(queue, (distance[next_node], next_node))
    
    return distance

answer = 0
for n in range(1, 1+N):
    go = dijkstra(n)
    back = dijkstra(X)
    answer = max(answer, go[X] + back[n])

print(answer)
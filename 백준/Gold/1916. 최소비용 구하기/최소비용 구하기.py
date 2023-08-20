import sys
from heapq import heappush, heappop

INF = int(1e9)
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    adj[start].append((end, cost))
A, B = map(int, input().split())
distance = [INF] * (N+1)
def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, node = heappop(q)
        if distance[node] < cost: continue
        for dnode, dcost in adj[node]:
            ncost = cost + dcost
            if ncost < distance[dnode]:
                distance[dnode] = ncost
                heappush(q, (ncost, dnode)) 
dijkstra(A)
print(distance[B])
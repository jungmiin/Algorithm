import sys
from heapq import heappush, heappop
INF = int(1e9)
input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
adj = [[] for _ in range(p)]
distance = [INF] * (p)

for _ in range(w):
    node1, node2, width = map(int, input().split())
    adj[node1].append((node2, width))
    adj[node2].append((node1, width))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    while q:
        _, node = heappop(q)
        for nnode, cost in adj[node]:
            if distance[nnode] == INF:
                distance[nnode] = min(distance[node], cost)
                heappush(q, (distance[nnode], nnode))
            elif min(cost, distance[node]) > distance[nnode]:
                distance[nnode] = min(distance[node], cost)
                heappush(q, (distance[nnode], nnode))
                
dijkstra(c)
print(distance[v])
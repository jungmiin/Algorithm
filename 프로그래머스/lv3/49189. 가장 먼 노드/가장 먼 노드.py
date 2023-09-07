from collections import deque
def solution(n, edge):
    def dijkstra():
        q = deque()
        q.append(1)
        dest[1] = 0
        while q:
            node = q.popleft()
            for nnode in adj[node]:
                if dest[nnode] == INF:
                    q.append(nnode)
                    dest[nnode] = dest[node] + 1
    answer = 0
    INF = int(1e9)
    adj = [[] for _ in range(n+1)]
    dest = [INF]*(n+1)
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    dijkstra()
    dest[0] = -1
    max_num = max(dest)
    return dest.count(max_num)
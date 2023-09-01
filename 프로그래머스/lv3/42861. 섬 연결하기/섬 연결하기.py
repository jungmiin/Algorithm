

def solution(n, edges):
    answer = 0
    sorted_edges = sorted(edges, key=lambda edge : edge[2])
    parent = [i for i in range(n)]
    def find_parent(n):
        if parent[n] != n:
            parent[n] = find_parent(parent[n])
        return parent[n]
    def union_parent(n, m):
        n, m = find_parent(start), find_parent(end)
        if n >= m: parent[n] = m 
        else: parent[m] = n
    for edge in sorted_edges:
        start, end, cost = edge
        n, m = find_parent(start), find_parent(end)
        if n != m:
            union_parent(n, m)
            answer += cost
    return answer
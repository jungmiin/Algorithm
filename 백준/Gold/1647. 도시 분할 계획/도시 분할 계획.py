import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    answer = 0
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    graph = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    graph.sort()
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if b > a:
            parent[b] = a
        else:
            parent[a] = b
    def find_parent(x):
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]
    last_cost = 0
    for cost, node1, node2 in graph:
        if find_parent(node1) != find_parent(node2):
            union_parent(node1, node2)
            answer += cost
            last_cost = cost
    print(answer-last_cost)

for _ in range(TEST_CASE):
    solution()
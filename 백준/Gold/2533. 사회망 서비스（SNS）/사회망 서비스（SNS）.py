import sys
from collections import deque
input = sys.stdin.readline

TEST_CASE = 1# 테스트 케이스 수
# 3 3

# 한 노드의 자식과 부모가 모두 얼리어답터여야됨.

def solution():
    N = int(input().rstrip())
    adj = [list() for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    def bfs():
        visited = [False] * (N+1)
        queue = deque()
        for i in range(1, N+1):
            if len(adj[i]) == 1:
                queue.append(i)
        result = set()
        while queue:
            node = queue.popleft()
            for parent_node in adj[node]:
                for other_node in adj[parent_node]:
                    adj[other_node].remove(parent_node)
                    if len(adj[other_node]) == 1:
                        queue.append(other_node)
                adj[parent_node] = []
                result.add(parent_node)
        return result
    print(len(bfs()))

for _ in range(TEST_CASE):
    solution()
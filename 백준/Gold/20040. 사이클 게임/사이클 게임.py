import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    answer = 0
    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    def union_parent(a, b):
        a, b = find_parent(a), find_parent(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    for i in range(M):
        a, b = map(int, input().split())
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
        else:
            answer = i+1
            break
    print(answer)

for _ in range(TEST_CASE):
    solution()
from collections import deque
import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N, M = map(int, input().split())
    indegree = [0]*(N+1)
    students = [list() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        indegree[b] += 1
        students[a].append(b)
    def topology_sort():
        result = []
        queue = deque()
        for i in range(1, N+1):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            now = queue.popleft()
            result.append(now)
            for student in students[now]:
                indegree[student] -= 1
                if indegree[student] == 0:
                    queue.append(student)
        return ' '.join(map(str, result))
    print(topology_sort())

for _ in range(TEST_CASE):
    solution()
import sys
from collections import deque
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
# 10
# 20
# 14
# 18
# 17

def solution():
    N = int(input().rstrip())
    indegree = [0] * (N+1)
    buildings = [[] for _ in range(N+1)]
    costs = [0] * (N+1)
    for i in range(1, N+1):
        input_data = list(map(int, input().split()))[:-1]
        costs[i] = input_data[0]
        for data in input_data[1:]:
            buildings[data].append(i)
            indegree[i] += 1
    def toplogy_sort():
        result = [0] * (N+1)
        queue = deque()
        for i in range(1, N+1):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            now = queue.popleft()
            result[now] += costs[now]
            for building in buildings[now]:
                indegree[building] -= 1
                result[building] = max(result[now], result[building])
                if indegree[building] == 0:
                    queue.append(building)
        return result
    
    for result in toplogy_sort()[1:]:
        print(result)


for _ in range(TEST_CASE):
    solution()
from collections import defaultdict

def dfs(adj, node, costs):
    if node not in adj:
        costs[node] = 1
        return costs
    else:
        for skill in adj[node]:
            result = dfs(adj, skill, costs)
            costs[node] += result[skill]
    return costs

def solution(total_sp, skills):
    skill_cnt = len(skills)+1
    adj = defaultdict(list)
    find_start_node = [True for _ in range(skill_cnt+1)]
    start_node = 0
    # 인접 리스트 만들기
    for parent, child in skills:
        adj[parent].append(child)
        find_start_node[child] = False
    # 시작 노드 찾기
    for i in range(1, skill_cnt+1):
        if find_start_node[i] == True:
            start_node = i
            break
    costs = dfs(adj, start_node, [0 for _ in range(skill_cnt+1)])
    basic_point = total_sp // sum(costs[1:])
    return [cost*basic_point for cost in costs[1:]]

# 테스트 케이스
print("Correct") if solution(120, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]) == [40, 20, 20, 10, 10, 10, 10] else print("Not correct")
print("Correct") if solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]) == [44, 11, 33, 11, 11, 11] else print("Not correct")
print("Correct") if solution(121, [[2, 1], [2, 3], [3, 6], [3, 4], [3, 5]]) == [11, 44, 33, 11, 11, 11] else print("Not correct")
print("Correct") if solution(121, [[2, 1], [2, 3], [3, 6], [3, 4], [3, 5]]) == [11, 44, 33, 11, 11, 11] else print("Not correct")
print("Correct") if solution(170, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5], [4, 7], [4, 8], [5, 9]]) == [50, 10, 40, 20, 10, 10, 10, 10, 10] else print("Not correct")
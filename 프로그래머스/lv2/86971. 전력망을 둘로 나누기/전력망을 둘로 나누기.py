from collections import deque
import copy

def search(adj, i):
    queue = deque()
    # print(i, "search")
    queue.append(adj[i])
    visit_set = set()
    visit_set.add(i)
    while queue:
        now = queue.popleft()
        for n in now:
            if n not in visit_set:
                visit_set.add(n)
                queue.append(adj[n])
    return len(visit_set)
    

def solution(n, wires):
    adj = [[] for _ in range(n+1)]
    answer = 1e9
    
    for wire in wires:
        v1, v2 = wire
        adj[v2].append(v1)
        adj[v1].append(v2)
    
    for wire in wires:
        v1, v2 = wire
        adj_copy = copy.deepcopy(adj)
        # print(adj_copy)
        del adj_copy[v1][adj[v1].index(v2)]
        del adj_copy[v2][adj[v2].index(v1)]
        # print(adj_copy)
        v1_length = search(adj_copy, v1)
        v2_length = search(adj_copy, v2)
        answer = min(answer, abs(v1_length-v2_length))
    
    return answer
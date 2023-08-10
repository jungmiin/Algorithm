def solution(info, edges):
    answer = []
    visited = [False for _ in range(len(info))]
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)  
        else: return
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                dfs(sheep, wolf+1) if info[c] else dfs(sheep+1, wolf)
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
    return max(answer)
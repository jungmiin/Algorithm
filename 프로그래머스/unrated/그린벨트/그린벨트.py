from collections import deque
dr = [0, 1]
dc = [1, 0]

def solution(N, trees):
    answer = 0
    graph = [list(0 for _ in range(N)) for _ in range(N)]
    
    for r,c in trees:
        graph[r][c] = 1
        r_cur = r+1
        c_cur = c+1
        while r_cur < 5:
            graph[r_cur][c] = 2
            r_cur+=1
        while c_cur < 5:
            graph[r][c_cur] = 2
            c_cur+=1

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0:
                for k in range(2):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if nr < N and nc < N and graph[nr][nc] == 1:
                        graph[nr][nc] = -1
                        answer += 1

    return answer

print("Correct") if solution(5, [[4, 3], [3, 1], [2, 2], [1, 4]]) == 3 else print("Not correct")
print("Correct") if solution(5, [[3, 3], [2, 2], [1, 1]]) == 1 else print("Not correct")

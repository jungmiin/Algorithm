dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1] 
# D L U R 오른쪽 회전은 +1 왼쪽 회전은 -1
def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    count = 0
    # print(visited, visited[0][0][0])
    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    nr, nc, nd = r, c, d
                    count = 0
                    while not visited[nr][nc][nd]:
                        count += 1
                        visited[nr][nc][nd] = True
                        nr, nc = (nr+dr[nd])%n, (nc+dc[nd])%m
                        if grid[nr][nc] == 'L':
                            nd = (nd - 1) % 4
                        elif grid[nr][nc] == 'R':
                            nd = (nd + 1) % 4
                    answer.append(count)
    return sorted(answer)
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    def bfs(i, j):
        dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]
        queue = deque()
        queue.append((i, j))
        cost = int(maps[i][j])
        maps[i] = maps[i][:j] + "X" + maps[i][j+1:]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != 'X':
                    queue.append((nr, nc))
                    cost += int(maps[nr][nc])
                    maps[nr] = maps[nr][:nc] + "X" + maps[nr][nc+1:]
        return cost
    answer = []
    for r in range(n):
        for c in range(m):
            if maps[r][c] != "X":
                answer.append(bfs(r, c))
    return [-1] if not len(answer) else sorted(answer)
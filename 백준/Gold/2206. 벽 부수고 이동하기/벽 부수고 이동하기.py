import sys
from collections import deque

def bfs(graph):
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  queue = deque()
  queue.append((0, 0, 0))
  visited[0][0][0] = 1
  while queue:
    x, y, is_crash = queue.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][is_crash]
    for i in range(4):
      tx = x + dx[i]
      ty = y + dy[i]
      if 0 <= tx < n and 0 <= ty < m:
        if graph[tx][ty] == 0 and visited[tx][ty][is_crash] == 0:
          queue.append([tx, ty, is_crash])
          visited[tx][ty][is_crash] = visited[x][y][is_crash] + 1
        if graph[tx][ty] == 1 and is_crash == 0:
          queue.append([tx, ty, 1])
          visited[tx][ty][1] = visited[x][y][0] + 1
        
  return -1

n, m = map(int, sys.stdin.readline().split())
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

answer = bfs(graph) # answer = min(answer, tmp_answer)

print(answer)
    

  
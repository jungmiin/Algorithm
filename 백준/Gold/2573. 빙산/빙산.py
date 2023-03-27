import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, visited):
  queue = deque()
  queue.append((i, j))
  visited[i][j] = 1
  melt_queue = deque()
  while queue:
    x, y = queue.popleft()
    melt_cnt = 0
    for t in range(4):
      tx = x + dx[t]
      ty = y + dy[t]
      if 0 <= tx < N and 0 <= ty < M and visited[tx][ty] == 0:
        if graph[tx][ty] > 0:
          visited[tx][ty] = 1
          queue.append((tx, ty))
        elif graph[tx][ty] == 0:
          melt_cnt += 1
    if melt_cnt:
      melt_queue.append((x, y, melt_cnt))
  return melt_queue
        
        
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

year = 0

while True:
  cnt = 0
  visited = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(N-1):
    for j in range(M-1):
      if graph[i][j] != 0 and visited[i][j] == 0:
        cnt += 1
        melt_queue = bfs(i, j, visited)
        while melt_queue :
          x, y, melt_cnt = melt_queue.popleft()
          graph[x][y] = max(graph[x][y]-melt_cnt, 0)
  if cnt == 0:
    year = 0
    break
  if cnt >= 2:
    break
  year += 1
print(year)
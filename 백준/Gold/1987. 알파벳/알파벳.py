#https://www.acmicpc.net/problem/1987
import sys
from string import ascii_uppercase

def bfs():
  queue = set([(0, 0, graph[0][0])])
  max_move = 1
  while queue:
    x, y, string = queue.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in string :
        queue.add((nx, ny, string + graph[nx][ny]))
        max_move = max(max_move, len(string) + 1)
  return max_move

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

print(bfs())
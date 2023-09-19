import sys
from copy import deepcopy
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수
directions = ["up", "down", "left", "right"]
answer = 0

def solution():
    N = int(input().rstrip())
    graph = [list(map(int, input().split())) for _ in range(N)]
    def combine(direction, graph):
        if direction == "up":
            for c in range(N):
                top = 0
                for r in range(1, N):
                    if graph[r][c] != 0:
                        number = graph[r][c]
                        graph[r][c] = 0
                        if graph[top][c] == 0:
                            graph[top][c] = number
                        else:
                            if graph[top][c] == number:
                                graph[top][c] *= 2
                            else:
                                graph[top+1][c] = number
                            top += 1
        elif direction == "down":
            for c in range(N):
                bottom = N-1
                for r in range(N-2, -1, -1):
                    if graph[r][c] != 0:
                        number = graph[r][c]
                        graph[r][c] = 0
                        if graph[bottom][c] == 0:
                            graph[bottom][c] = number
                        else:
                            if graph[bottom][c] == number:
                                graph[bottom][c] *= 2
                            else:
                                graph[bottom-1][c] = number
                            bottom -= 1
        elif direction == "right":
            for r in range(N):
                right = N-1
                for c in range(N-2, -1, -1):
                    if graph[r][c] != 0:
                        number = graph[r][c]
                        graph[r][c] = 0
                        if graph[r][right] == 0:
                            graph[r][right] = number
                        else:
                            if graph[r][right] == number:
                                graph[r][right] *= 2
                            else:
                                graph[r][right-1] = number
                            right -= 1
        elif direction == "left":
            for r in range(N):
                left = 0
                for c in range(1, N):
                    if graph[r][c] != 0:
                        number = graph[r][c]
                        graph[r][c] = 0
                        if graph[r][left] == 0:
                            graph[r][left] = number
                        else:
                            if graph[r][left] == number:
                                graph[r][left] *= 2
                            else:
                                graph[r][left+1] = number
                            left += 1
        return graph
    
    def move(num, graph):
        global answer
        if num == 0:
            for i in range(N):
                for j in range(N):
                    answer = max(graph[i][j], answer)
            return
        for d in range(4):
            copy_graph = deepcopy(graph)
            copy_graph = combine(directions[d], copy_graph)
            move(num-1, copy_graph)
    
    move(5, graph)

    print(answer)

for _ in range(TEST_CASE):
    solution()
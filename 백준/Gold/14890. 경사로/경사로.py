# 경사로

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def search(road):
    for i in range(1, N):
        if abs(road[i] - road[i-1]) > 1:
            return False
        elif road[i] < road[i-1]: # 오르막길
            for j in range(L):
                if i+j >= N or road[i] != road[i+j] or used[i+j]:
                    return False
                used[i+j] = True 
        elif road[i] > road[i-1]: # 내리막길
            for j in range(1, L+1):
                if i-j < 0 or road[i-1] != road[i-j] or used[i-j]:
                    return False
                used[i-j] = True 
    return True

# 가로
for i in range(N):
    used = [False for _ in range(N)]
    if search(graph[i]):
        # print("가로", i)
        answer += 1
for i in range(N):
    used = [False for _ in range(N)]
    if search([graph[j][i] for j in range(N)]):
        # print("세로", i)
        answer+=1

print(answer)
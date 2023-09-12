import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

# 5 5 0

def solution():
    answer = 0
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))
    max_height, max_cur = 0, 0
    for i in range(W):
        if i > max_cur+1 and blocks[i] > 0:
            for j in range(max_cur+1, i):
                if blocks[j] < min(max_height, blocks[i]):
                    answer += min(max_height, blocks[i]) - blocks[j]
                    blocks[j] = min(max_height, blocks[i])
        if blocks[i] >= max_height:
            max_height = blocks[i]
            max_cur = i
    print(answer)
for _ in range(TEST_CASE):
    solution()
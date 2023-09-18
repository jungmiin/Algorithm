import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N = int(input().rstrip())
    weights = list(map(int, input().split()))
    weights.sort()
    answer = 0
    for weight in weights:
        if answer+1 >= weight:
            answer += weight
        else:
            break
    print(answer+1)

for _ in range(TEST_CASE):
    solution()
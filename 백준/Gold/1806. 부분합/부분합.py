import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    value = numbers[0]
    scope = [0, 1]
    answer = N+1
    if sum(numbers) < S:
        answer = 0
    else:
        while scope[0] <= scope[1]:
            if value >= S:
                if scope[0] == scope[1]:
                    answer = 1
                    break
                else:
                    answer = min(scope[1]-scope[0], answer)
                    value -= numbers[scope[0]]
                    scope[0] += 1
            elif scope[1] < N:
                value += numbers[scope[1]]
                scope[1] += 1
            else: 
                break
    print(answer)
for _ in range(TEST_CASE):
    solution()
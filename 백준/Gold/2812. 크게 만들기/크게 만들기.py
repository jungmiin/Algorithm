# 크게 만들기

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(input().rstrip())

stack = []

for number in numbers:
    while stack and stack[-1] < number and K>0:
        stack.pop()
        K -= 1
    stack.append(number)

print(''.join(stack[:len(stack)-K]))
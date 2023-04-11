# 기념품

from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())

people = deque(range(1, N+1))
stage = 1

while len(people) > 1:
    people.rotate(-(stage ** 3 - 1))
    people.popleft()
    stage += 1

print(people[0])
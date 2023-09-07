import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(n, m):
    n, m = find(n), find(m)
    if n > m:
        parent[n] = m
    else:
        parent[m] = n

N = int(input().rstrip())
M = int(input().rstrip())

parent = [i for i in range(N+1)]

for i in range(1, N+1):
    l = list(map(int, input().split()))
    for j in range(1, N+1):
        if l[j-1] == 1:
            union(i, j)

city = list(map(int, input().split()))
p = find(city[0])
for i in city[1:]:
    if p != find(i):
        print("NO")
        exit()
print("YES")
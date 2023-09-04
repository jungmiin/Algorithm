import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

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

for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    elif x == 1:
        pa, pb = find(a), find(b)
        print("YES") if pa == pb else print("NO")

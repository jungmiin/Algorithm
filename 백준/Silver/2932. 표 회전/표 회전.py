import sys
input = sys.stdin.readline
N, K = map(int,input().split())

data = []
for _ in range(K):
    X, R, C = map(int,input().split())
    data.append([X, (X-1)//N , (X-1) % N  , R-1, C-1]) 

def rotate(i, mr, mc, n, tr, tc, r, c):       
    for j in range(i+1, K):
         if  data[j][0] == n:
             data[j][1] = r
             data[j][2] = c
         else:
             if data[j][1] == tr:
                 data[j][2] += mc
                 if data[j][2] >= N:
                     data[j][2] %= N
             if data[j][2] == c:
                 data[j][1] += mr
                 if data[j][1] >= N:
                     data[j][1] %= N

for i, d in enumerate(data): 
    n, tr, tc, r, c = d
    answer = 0
    mr = r - tr if r >= tr else r - tr + N
    mc = c - tc if c >= tc else c - tc + N 
    answer = answer + mr + mc
    rotate(i, mr, mc, n, tr, tc, r, c)
    print(answer) 
    
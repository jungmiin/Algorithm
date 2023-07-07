# LCS
import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

def lcs(s1, s2):
    dp = [[None] * (len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else :
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[len(s1)][len(s2)]

print(lcs(s1,s2))
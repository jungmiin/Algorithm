import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    strings = [input().rstrip() for _ in range(3)]
    s1, s2, s3 = strings[0], strings[1], strings[2]
    dp = [[[0] * (len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            for k in range(1, len(s3)+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    print(dp[-1][-1][-1])
for _ in range(TEST_CASE):
    solution()
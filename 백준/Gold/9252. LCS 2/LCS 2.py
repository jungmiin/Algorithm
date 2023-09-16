import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

def solution():
    string1 = [""]+list(input().rstrip())
    string2 = [""]+list(input().rstrip())
    LCS = [[""]*len(string2) for _ in range(len(string1))]
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                LCS[i][j] = LCS[i-1][j-1] + string1[i]
            else:
                if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                    LCS[i][j] = LCS[i-1][j]
                else:
                    LCS[i][j] = LCS[i][j-1]
    result = LCS[-1][-1]
    print(len(result), result, sep="\n")

for _ in range(TEST_CASE):
    solution()
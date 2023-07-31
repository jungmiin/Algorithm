from collections import defaultdict

def solution(s):
    s_split = [list(map(int, ss.split(","))) for ss in s[2:-2].split("},{")]
    dic = defaultdict(int)
    for li in s_split:
        for l in li:
            dic[l] += 1

    return [num[0] for num in sorted(dic.items(), key = lambda item: item[1], reverse=True)]
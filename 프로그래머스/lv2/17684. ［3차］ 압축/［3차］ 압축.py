
from collections import deque

ascii_num = 64
alpha_num = 26
def solution(msg):
    answer = []
    dictionary = {}
    msg_list = deque(list(msg))
    # 리스트를 돌면서
    # 해당 문자가 사전에 있는지 검사
    # 만약 있다면
    # 뒤에 문자까지 붙여서 검사 (없을 때까지 반복)
    # 최대 문자열 색인 찾아낸 뒤 answer에 append
    # 이후 리스트에 해당 문자들 지우기
    # 이랬을때도 리스트가 남아있다면
    # 해당 문자까지 붙여서 색인에 추가하기
    
    while msg_list:
        tmp = ""
        tmp += msg_list.popleft()
        while msg_list and tmp + msg_list[0] in dictionary:
            tmp += msg_list.popleft()
        index = ord(tmp) - ascii_num if len(tmp) == 1 else dictionary[tmp]
        answer.append(index)
        if msg_list and tmp + msg_list[0] not in dictionary:
            dictionary[tmp + msg_list[0]] = alpha_num + len(dictionary) + 1
            
    return answer
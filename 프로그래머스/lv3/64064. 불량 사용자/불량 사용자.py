from collections import deque
def bfs(user_ids, banned_ids):
    queue = deque()
    queue.append((0, []))
    result = []
    while queue:
        ban_idx, ids = queue.popleft()
        if ban_idx >= len(banned_ids):
            result.append(ids)
            continue
        banned_id = banned_ids[ban_idx]
        masking = []
        for i, char in enumerate(banned_id):
            if char == '*': masking.append(i)
        for user_id in user_ids:
            if len(user_id) != len(banned_id): continue
            new_user_id = user_id
            for i in masking: new_user_id = new_user_id[:i] + '*' + new_user_id[i+1:]
            if new_user_id == banned_id and user_id not in ids:
                new_ids = ids + [user_id]
                queue.append((ban_idx+1, new_ids))
    return result

def solution(user_ids, banned_ids):
    answer = set()
    result = bfs(user_ids, banned_ids)
    for res in result:
        answer.add(','.join(sorted(res)))
    return len(answer)
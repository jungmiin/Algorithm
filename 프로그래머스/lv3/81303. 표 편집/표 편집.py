class Node :
    def __init__(self, left = None, right = None):
        self.is_deleted = False
        self.left = left
        self.right = right

def solution(n, k, cmds):
    answer = ''
    table = [ Node(i-1, i+1) for i in range(n)]
    table[0].left = None
    table[n-1].right = None
    buffer = []
    
    for cmd in cmds:
        if cmd[0] == "U":
            _, num = cmd.split()
            for _ in range(int(num)):
                k = table[k].left
        elif cmd[0] == "D":
            _, num = cmd.split()
            for _ in range(int(num)):
                k = table[k].right
        elif cmd[0] == "C":
            buffer.append(k)
            table[k].is_deleted = True
            left, right = table[k].left, table[k].right
            if left != None:
                table[left].right = right
            if right != None:
                table[right].left = left
                k = right
            else: 
                k = left
        elif cmd[0] == "Z":
            z = buffer.pop()
            table[z].is_deleted = False
            left, right = table[z].left, table[z].right
            if left != None:
                table[left].right = z
            if right != None:
                table[right].left = z
                
    for node in table:
        if node.is_deleted: answer += "X"
        else: answer += "O"
        
    return answer
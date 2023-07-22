import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])
List  = []
for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] in 'push':
        q.append(int(order[1]))
    elif order[0] in 'front':
        if len(q) ==0:
            List.append(-1)
        else :
            List.append(q[0])
    elif order[0] in 'back':
        if len(q) ==0:
            List.append(-1)
        else :
            List.append(q[-1])
    elif order[0] in 'size':
        List.append(len(q))
    elif order[0] in 'pop':
        if len(q) ==0:
            List.append(-1)
        else:
            List.append(q.popleft())

    elif order[0] in 'empty':
        if len(q) ==0:
            List.append(1)
        else:
            List.append(0)

for i in range(len(List)):
    print(List[i])
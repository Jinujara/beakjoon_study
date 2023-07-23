import sys
n,m = map(int,sys.stdin.readline().split())
A, B= [],[]
for i in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))

m,k = map(int,sys.stdin.readline().split())
for i in range(m):
    B.append(list(map(int,sys.stdin.readline().split())))
C = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        row = 0
        for l in range(m):
            row+= A[i][l]*B[l][j]
        C[i][j] = row
for i in range(len(C)):
    print(*C[i])
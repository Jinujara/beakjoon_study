import sys
p_num, n = map(int,sys.stdin.readline().split())
pocket = [i for i in range(1,p_num+1)]
temp = 0
for a in range(n):
    i, j = map(int,sys.stdin.readline().split())
    temp = pocket[i-1]
    pocket[i-1] = pocket[j-1]
    pocket[j-1] = temp
for b in range(len(pocket)):
    if b == len(pocket)-1:
        print(pocket[b],end = '')
    else:
        print(pocket[b],end=' ')
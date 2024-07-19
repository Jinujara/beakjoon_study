import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

hash = {}
for num in N_list:
    if num in hash:
        hash[num] +=1
    else:
        hash[num] = 1

for num in M_list:
    if num in hash:
        print(hash[num],end=" ")
    else:
        print(0,end=" ")
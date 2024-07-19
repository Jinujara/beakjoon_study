from collections import Counter
import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

count = Counter(N_list)

for num in M_list:
    if num in count:
        print(count[num], end = " ")
    else:
        print(0,end= " ")
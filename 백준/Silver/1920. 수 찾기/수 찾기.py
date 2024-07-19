import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A.sort()
for num in B:
    start = 0
    end = N-1
    exist=0
    while(start <=end):
        mid = (start+end) // 2
        if (num > A[mid]):
            start = mid+1
        elif(num < A[mid]):
            end = mid-1
        else:
            exist = 1
            break

    print(exist)
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
find = int(sys.stdin.readline())
cnt = a.count(find)
print(cnt)

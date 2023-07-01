import sys
a = int(sys.stdin.readline())

for i in range(a):
    for j in range(i):
        print(" ", end='')
    for j in range(2*(a-i-1)+1):
        print("*", end='')
    print()
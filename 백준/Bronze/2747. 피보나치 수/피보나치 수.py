import sys
n= int(sys.stdin.readline())
a,b = 0,1
c=0
if n == 0:
    print(0)
elif n== 1:
    print(1)
else:
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    print(c)
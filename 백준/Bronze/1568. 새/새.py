import sys
birds = int(sys.stdin.readline())
num = 1
count = 0
while birds>0:
    if birds <num:
        num=1
    birds -= num
    num+=1
    count+=1
print(count)

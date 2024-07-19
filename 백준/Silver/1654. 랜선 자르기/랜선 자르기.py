from sys import stdin

K,N = map(int,stdin.readline().split())
list = [int(stdin.readline()) for _ in range(K)]

list.sort()
start = 1
end = list[-1]

while start <= end:
    mid = (start+end)//2
    result = 0
    for i in list:
        result += i//mid
    if result >= N:
        start = mid+ 1
    else:
        end = mid -1
print(end)
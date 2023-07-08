import sys
n = int(sys.stdin.readline())
List = []
for i in range(n):
    List.append(int(sys.stdin.readline()))
List = sorted(List)
for j in range(len(List)):
    print(List[j], end = '\n')
import sys
n = int(sys.stdin.readline())
List = []
for i in range(n):
    k,h = map(int,sys.stdin.readline().split())
    List.append((k,h))
Rank = []
for i in range(n):
    rank = 1
    for j in range(n):
        if List[i][0] < List[j][0] and List[i][1] < List[j][1]: # 자신이 더 작을 경우,
            rank +=1
        else:
            continue
    Rank.append(rank)
print(*Rank)
n = int(input())
List = []
for i in range(n):
    List.append(int(input()))
List = sorted(List)
for j in range(len(List)):
    print(List[j])
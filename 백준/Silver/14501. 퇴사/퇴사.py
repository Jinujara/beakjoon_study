import sys

def dfs(today,pay_sum):
    global answer
    if today==n:
        answer = max(answer,pay_sum)
        return
    pay = List[today][1]
    next_day = today + List[today][0]
    if next_day <=n:
        dfs(next_day,pay_sum+pay)
    dfs(today+1,pay_sum)

n = int(sys.stdin.readline())
List = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer = 0
for i in range(n):
    dfs(i,0)
print(answer)
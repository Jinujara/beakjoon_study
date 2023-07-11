import sys
n = int(sys.stdin.readline())
List = []
# 3자리숫자. 겹치지 않는.
for first in range(1,10):
    for second in range(1,10):
        for third in range(1,10):
            if first == second or first== third or second == third:
                continue
            else:
                List.append(str(first)+str(second) + str(third))
for _ in range(n):
    guess, strike, ball = map(int,sys.stdin.readline().split())
    guess = list(str(guess))
    rmcnt = 0
    for k in range(len(List)):
        s = b = 0
        k-= rmcnt # List[0] 부터 시작.
        for j in range(3):
            if List[k][j] == guess[j]:
                s += 1
            elif guess[j] in List[k]:
                b += 1
        if(s != strike) or (ball != b):
            List.remove(List[k])
            rmcnt+=1
print(len(List))
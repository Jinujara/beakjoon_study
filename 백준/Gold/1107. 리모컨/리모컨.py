start = 100
N = int(input())  # 이동하려는 채널
EB_cnt = int(input()) # 고장난 버튼의 갯수
button = [str(i) for i in range(10)]
if EB_cnt !=0: #고장난 버튼이 0개이면 입력받지 않음.
    EB_list = list(input().split())
    for i in range(EB_cnt):
        button.remove(EB_list[i])

min_cnt = abs(start-N)

for i in range(1000000): # 모든 숫자에 대해서
    num = str(i)
    for k in range(len(num)): #
        if num[k] not in button: # 누를 수 있는 버튼이 없을 때
            break
        if k == len(num)-1:
            min_cnt = min(min_cnt, abs(N-i)+len(num))
print(min_cnt)
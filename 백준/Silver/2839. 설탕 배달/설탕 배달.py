kig = int(input())
count = 0
while kig>=0:
    if kig %5 ==0:
        count += int(kig//5)
        print(count)
        break

    kig -= 3
    count +=  1
else:
    print(-1)
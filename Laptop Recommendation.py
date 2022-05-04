#Subscribe to channel = https://bit.ly/3F4Jxnd
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    rem = [0]*(11)
    for i in A:
        rem[i] += 1
    cur_max = 0
    flag = False
    for i in range(len(rem)):
        if rem[cur_max] < rem[i] :
            cur_max = i
            flag = False
        elif rem[cur_max] == rem[i]:
            flag = True
    if flag:
        print('Confused')
    else:
        print(cur_max)

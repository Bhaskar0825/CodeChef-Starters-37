#Subscribe to channel = https://bit.ly/3F4Jxnd
T = int(input())
import math
for _ in range(T):
    n,x = map(int,input().split())
    A = list(map(int,input().split()))
    multi_target_time = max(A)
    single_target_time = 0
    for i in A:
        if i <=x:
            single_target_time += 1 
        else:
            single_target_time += math.ceil(i/x)
    print(min(multi_target_time,single_target_time))

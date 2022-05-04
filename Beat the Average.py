#Subscribe to channel = https://bit.ly/3F4Jxnd
for i in range(int(input())):
    N,M,X = map(int,input().split())
    z1 = N*X
    z2 = X+1
    if z2>M:
        print(0)
    else:
        print(z1//z2)

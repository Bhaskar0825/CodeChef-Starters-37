#Subscribe to channel = https://bit.ly/3F4Jxnd
for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    s = sum(nums) * 2
    if s % n == 0 and (s // n) % 2 == 1:
        print("Yes")
    else:
        print("No")

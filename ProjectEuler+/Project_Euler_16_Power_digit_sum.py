for _ in range(int(input())):
    n = int(input())
    sn = str(2**n)
    ans = 0
    for d in sn:
        ans += int(d)
    print(ans)

#Problem ID: EID
#Problem Name: Chef and Eid

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    diff = abs(l[0] - l[1])

    for i in range(2, n):
        x = abs(l[i-1] - l[i])
        if x < diff:
            diff = x
    print(diff)

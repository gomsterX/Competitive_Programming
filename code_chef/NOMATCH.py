#Problem ID: NOMATCH
#Problem Name: Maximise the Sum

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print(sum(l[n//2:]) - sum(l[:n//2]))

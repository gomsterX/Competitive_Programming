#Problem ID: CASH
#Problem Name: Hard Cash

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    print(sum(l)%k)

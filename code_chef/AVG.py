#Problem ID: AVG
#Problem Name: Average Number

for _ in range(int(input())):
    n, k, v = map(int, input().split())
    l = list(map(int, input().split()))

    x = ((v*(k+n)) - sum(l))/k
    x = x if x > 0 and x%1 == 0 else -1

    print(int(x))

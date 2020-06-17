#Problem ID: RRJOKE
#Problem Name: Good Joke!

for _ in range(int(input())):
    ans = 0
    n = int(input())
    for i in range(n):
        list(map(int, input().split()))

    for i in range(n+1):
        ans=ans ^ i
    print(ans)


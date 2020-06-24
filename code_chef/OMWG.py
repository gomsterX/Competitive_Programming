#Problem ID: OMWG
#Problem Name: One more weird game

for _ in range(int(input())):
    n, m = map(int, input().split())

    print((n-1)+(m-1)+((n-1)*(m-1)*2))

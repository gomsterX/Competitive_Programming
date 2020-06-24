#Problem ID: UTMOPR
#Problem Name: Strange operations

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if(k>1):
        print("even")
    else:
        print("odd")



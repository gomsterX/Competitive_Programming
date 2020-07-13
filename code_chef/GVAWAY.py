#Problem ID: GVAWAY
#Problem Name: Is This a Give Away

for _ in range(int(input())):
    l, r, k = map(int, input().split())
    print(1) if l == r else print(k)

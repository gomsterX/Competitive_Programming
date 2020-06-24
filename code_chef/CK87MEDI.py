#Problem ID: CK87MEDI
#Problem Name: Chef and Employment Test

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = sorted(list(map(int, input().split())))
    print(l[(n+k)//2])

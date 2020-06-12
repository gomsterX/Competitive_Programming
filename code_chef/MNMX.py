#Problem ID: MNMX
#Problem Name: Minimum Maximum

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(arr[0] * (n-1))

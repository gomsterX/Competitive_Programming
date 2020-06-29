#Problem ID: DEVARRAY
#Problem Name: Devu and an Array

n, q = map(int, input().split())
l = list(map(int, input().split()))
min_number = min(l)
max_number = max(l)
for i in range(q):
    if(min_number <= int(input()) <= max_number):
        print("Yes")
    else:
        print("No")


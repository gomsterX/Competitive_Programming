#Problem ID: MAXREM
#Problem Name: Maximum Remaining

n = int(input())
l = list(map(int, input().split()))
mx = l[0]
mx2 = l[0]
for i in range(1, n):
    if(l[i] > mx):
        mx2 = mx
        mx = l[i]
print(mx2%mx)


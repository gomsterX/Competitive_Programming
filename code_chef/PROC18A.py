#Problem ID: PROC18A
#Problem Name: The Great Run

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = l[0]
    for i in range(n):
        if(i+k <=n):
            s = max(s, sum(l[i:i+k]))
    print(s)

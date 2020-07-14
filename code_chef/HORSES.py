#Problem ID: HORSES
#Problem Name: Racing Horses

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    m = l[1]-l[0]
    for i in range(1, n-1):
        m = min(m, l[i+1]-l[i])
    print(m)

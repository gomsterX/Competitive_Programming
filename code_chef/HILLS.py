#Problem ID: HILLS
#Problem Name: Jumping in the hills

for _ in range(int(input())):
    n, u, d = map(int, input().split())
    l = list(map(int, input().split()))
    par = True
    i = 0
    while i<n-1:
        if l[i+1] > l[i] and l[i+1]-l[i] > u:
            break
        elif l[i+1] < l[i] and l[i] - l[i+1] > d:
                if par:
                    par = False
                else:
                    break
        i += 1

    print(i + 1)

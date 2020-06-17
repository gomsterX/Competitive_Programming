#Problem ID: MOVIEWKN
#Problem Name: Movie Weekend

for _ in range(int(input())):
    n = int(input())
    l_max = 0
    r_max = 0
    index = 0
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    for i in range(n):
        if(l[i] * r[i] > l_max * r_max
                or(l[i]*r[i] == l_max*r_max and r[i] > r_max)):
            l_max = l[i]
            r_max = r[i]
            index = i

    print(index + 1)

#Problem ID: SWPDGT
#Problem Name: Chef Swaps Digits

for _ in range(int(input())):
    s1 = list(input().split())
    s2, s1 = list(s1[1]), list(s1[0])

    mx = int(''.join(s1)) + int(''.join(s2))
    for i in range(len(s1)):
        for j in range(len(s2)):
            x = s1[:]
            y = s2[:]
            x[i], y[j] = y[j], x[i]
            mx = max(mx, int(''.join(x)) + int(''.join(y)))
    print(mx)


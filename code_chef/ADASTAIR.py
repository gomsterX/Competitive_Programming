#Problem ID: ADASTAIR
#Problem Name: Ada and the Staircase

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    pos = 0
    steps = 0
    for i in l:
        if i - pos <= k:
            pos = i
        else:
            steps += ((i-pos)//k)
            if (i-pos)%k == 0:
                steps -= 1
            pos = i
    print(steps)

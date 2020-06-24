#Problem ID: TEMPLELA
#Problem Name: Temple Land

for _ in range(int(input())):
    s = True
    n = int(input())
    tms = list(map(int, input().split()))

    if n % 2 == 0:
        s = False
    else:
        for i in range(1, int(n/2) + 2):
            if(tms[i-1] != i) or (tms[n - i] != i):
                s = False
                break

    if(s):
        print("yes")
    else:
        print("no")

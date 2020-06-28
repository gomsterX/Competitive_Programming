#Problem ID: WDTBAM
#Problem Name: Who dares to be a millionaire

for _ in range(int(input())):
    n = int(input())
    q = input()
    ans = input()
    w = list(map(int, input().split()))
    c = 1
    if q == ans:
        print(w[-1])
    else:
        for i in range(n):
            if(q[i] == ans[i]):
                c +=1
        print(max(w[:c]))

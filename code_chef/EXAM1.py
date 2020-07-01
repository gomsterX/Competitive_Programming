#Problem ID: EXAM1
#Problem Name: Multiple Choice Exam

for _ in range(int(input())):
    n = int(input())
    i = 0
    q = list(input())
    ans = list(input())
    res = 0
    while i < n:
        if q[i] == ans[i]:
            res += 1
            i+=1
        elif ans[i] == 'N':
            i+=1
        else:
            i+=2
    print(res)

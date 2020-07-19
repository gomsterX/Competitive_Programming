#Problem ID: CHFICRM
#Problem Name: Chef and Icecream

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    cn_5 = 0
    cn_10 = 0
    al = True
    for i in range(n):
        if l[i] == 5:
            cn_5+=5
        elif l[i] == 10:
            if cn_5 >0:
                cn_5 -= 5
                cn_10 += 10
            else:
                al = False
                break
        else:
            if cn_10 >0:
                cn_10 -= 10
            elif cn_5 >= 10:
                cn_5 -= 10
            else:
                al = False
                break
    print('YES') if al else print('NO')

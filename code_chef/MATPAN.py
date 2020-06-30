#Problem ID: MATPAN
#Problem Name: Mathison and pangrams

alp = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    p = list(map(int, input().split()))
    l = input()

    m = 0
    for i in alp:
        if i not in l:
            m += p[(ord(i) - ord('a'))]

    print(m)


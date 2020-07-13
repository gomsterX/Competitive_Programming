#Problem ID: SC31
#Problem Name: Weapon Value

for _ in range(int(input())):
    n = int(input())
    s = []
    c = 0
    for i in range(n):
        s.append(input())
    for j in range(10):
        weap = 0
        for i in range(n):
            weap = weap +1 if s[i][j] == '1' else weap
        if weap%2 != 0:
            c+=1
    print(c)

#Problem ID: REDONE
#Problem Name: Reduce to One
x = 0
l = []
for i in range(1000020):
    x = (x*i + x + i)%1000000007
    l.append(x)
for _ in range(int(input())):
    print(l[int(input())])

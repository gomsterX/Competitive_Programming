#Problem ID: XYSTR
#Problem Name: Chef and String

for _ in range(int(input())):
    n = input()
    c = n.count('xy')
    n = n.replace('xy', '')
    print(c+n.count('yx'))

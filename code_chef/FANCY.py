#Problem ID: FANCY
#Problem Name: Fancy Quotes

for _ in range(int(input())):
    s = input().split()
    if ' not ' in s:
        print('Real Fancy')
    else:
        print('regularly fancy')

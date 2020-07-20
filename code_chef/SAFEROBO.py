#Problem ID: SAFEROBO
#Problem Name: Safe Robots

for _ in range(int(input())):
    s = input()
    sa, sb = map(int, input().split())
    a = s.index('A')
    b = s.index('B')
    safe = True
    while a <= b:
        if a == b:
            safe = False
        a+=sa
        b-=sb
    if safe:
        print('safe')
    else:
        print('unsafe')

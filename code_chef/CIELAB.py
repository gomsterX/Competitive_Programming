#Problem ID: CIELAB
#Problem Name: Ciel and A-B Problem

x, y = map(int, input().split())
x-=y
if x+1%10==0:
    print(x-1)
else:
    print(x+1)

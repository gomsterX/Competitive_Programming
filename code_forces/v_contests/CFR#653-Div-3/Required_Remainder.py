#Codeforces Round #653 (Div. 3)
#problem: A) Reqired Remainder

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    a = z%x

    z = z-a
    if(y <= a):
        z+=y
    else:
        z -= (x-y)

    print(z)

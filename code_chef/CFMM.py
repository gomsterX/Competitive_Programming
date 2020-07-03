#Problem ID: CFMM
#Problem Name: Making a Meal

for _ in range(int(input())):
    n = int(input())
    x = ''
    for i in range(n):
        x += input()
    print(min(x.count('c')//2, x.count('o'), x.count('d'), x.count('e')//2,
        x.count('h'), x.count('f')))

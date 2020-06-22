#Problem ID: BRACKETS
#Problem Name: Brackets

for _ in range(int(input())):
    a = input()

    b = 0
    mb = 0
    for i in a:
        if i == '(':
            b+=1
        elif i == ')':
            b-=1
        mb = max(b, mb)
    print('('*mb + ')'*mb)

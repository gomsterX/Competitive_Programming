#Problem ID: CHEFROUT
#Problem Name: Chef and his daily routine

for _ in range(int(input())):
    x = input()
    if('EC' in x or 'SE' in x or 'SC' in x):
        print('no')
    else:
        print('yes')

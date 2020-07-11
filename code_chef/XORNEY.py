#Problem ID: XORNEY
#Problem Name: XOR! Wait for it

for _ in range(int(input())):
    l, r = map(int, input().split())
    c =0
    if l%2 or r%2:
        c = (r-l)//2 +1
    else:
        c = (r-l)//2
    if c%2:
        print('Odd')
    else:
        print('Even')

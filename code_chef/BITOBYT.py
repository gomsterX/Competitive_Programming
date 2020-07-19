#Problem ID: BITOBYT
#Problem Name: Byte to Bit

for _ in range(int(input())):
    n = int(input())
    bits = nibs = byts = 0
    x = n//26
    y = n%26
    if y == 0:
        byts = 2**(x-1)
    elif y == 1 or y == 2:
        bits+= max(1, 2**x)
    elif y > 2 and y<= 10:
        nibs += max(1, 2**x)
    else:
        byts += max(1, 2**x)
    print(bits, nibs, byts)


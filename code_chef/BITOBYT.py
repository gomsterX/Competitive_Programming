#Problem ID: BITOBYT
#Problem Name: Byte to Bit

for _ in range(int(input())):
    n = int(input())
    bit = byt = nib = 0
    if (n>=24):
        bit = n//24
        n -= (n//24 * 24)
    if n >= 9:
        byt = n//9
        n -= (n//24 * 9)
    nib = n//3

    print(bit, nib, byt)

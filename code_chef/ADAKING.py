#Problem ID: ADAKING
#Problem Name: Ada King

for _ in range(int(input())):
    n = int(input())
    board = ['X']*64
    for i in range(1, n):
        board[i] = '.'
    board[0] = 'O'
    for i in range(64):
        if (i)%8 == 0:
            print()
        print(board[i], end = '')
    print()




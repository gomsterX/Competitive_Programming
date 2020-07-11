#Problem ID: ZUBREACH
#Problem Name: J - Reached Safely Or Not

for c in range(int(input())):
    m, n  = map(int, input().split())
    x, y = map(int, input().split())
    int(input())
    mov = input()
    posy, posx = mov.count('U')-mov.count('D'), mov.count('R')-mov.count('L')
    if posx == x and posy == y:
        print('Case {}: REACHED'.format(c+1))
    elif posx <0 or posx > m or posy < 0 or posy > n:
        print("Case {}: DANGER".format(c+1))
    else:
        print("Case {}: SOMEWHERE".format(c+1))


#Problem ID: COLOR
#Problem Name: Chef And Coloring

for _ in range(int(input())):
    n = int(input())
    color = input()
    R = color.count('R')
    G = color.count('G')
    B = color.count('B')

    x = max(R, G, B)
    print(n - x)

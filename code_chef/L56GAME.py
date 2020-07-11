#Problem ID: L56GAME
#Problem Name: Chef and Game with Sequence

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if i %2 != 0:
            c +=1
    if c%2 == 0 or len(l) == 1:
        print(1)
    else:
        print(2)

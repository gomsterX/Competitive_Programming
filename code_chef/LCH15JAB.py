#Problem ID: LCH15JAB
#Problem Name: Piece of cake



def check(x):
    for i in x:
        if x.count(i) == len(x)/2:
            print("YES")
            return 0
    print("NO")
for _ in range(int(input())):
    x = list(input())
    check(x)


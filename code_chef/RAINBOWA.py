#Problem ID: RAINBOWA
#Problem Name: Chef and Rainbow Array

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    rnbw = True
    if(a != a[::-1] or set(a) != {1, 2, 3, 4, 5, 6, 7}):
        rnbw = False
    print("yes") if rnbw else print("no")


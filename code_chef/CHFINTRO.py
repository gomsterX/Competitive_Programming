#Problem ID: CHFINTRO
#Problem Name: Chef and Interactive Contests

n, r = map(int, input().split())
for _ in range(n):
    if(int(input()) < r ):
        print("Bad boi")
    else:
        print("Good boi")

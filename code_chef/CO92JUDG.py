#Problem ID: CO92JUDG
#Problem Name: Chef Judges a Competition

for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = sum(a) - max(a)
    y = sum(b) - max(b)

    if(x<y):
        print("Alice")
    elif(y<x):
        print("Bob")
    else:
        print("Draw")

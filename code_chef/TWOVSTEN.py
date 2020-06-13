#Problem ID: TWOVSTEN
#Problem Name: Two vs Ten

for _ in range(int(input())):
    x = int(input())
    if(x % 5 != 0):
        print(-1)
    else:
        if(x % 10 == 0):
            print(0)
        else:
            print(1)

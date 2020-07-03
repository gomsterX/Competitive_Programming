#Problem ID: PAJAPONG
#Problem Name: Ping Paja Pong

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if(int((x+y)/k) %2 == 0):
        print("Chef")
    else:
        print("Paja")

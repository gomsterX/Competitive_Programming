#Problem ID: BRLADDER
#Problem Name: Bear and Ladder

for _ in range(int(input())):
    x, y = map(int, input().split())
    x, y = min(x,y), max(x,y)

    if(y-x == 2 or (y-x == 1 and x%2 != 0)):
        print("YES")
    else:
        print("NO")

#Problem ID: RECTANGL
#Problem Name: Rectangle

for _ in range(int(input())):
    numbers = sorted(list(map(int, input().split())))
    if (numbers[0] == numbers[1]
            and numbers[2] == numbers[3]):
        print("YES")
    else:
        print("NO")

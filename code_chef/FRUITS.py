#Problem ID: FRUITS
#Problem Name: Chef and Fruits

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    diff = abs(x-y)
    diff = 0 if (diff < z) else abs(diff - z)
    print(diff)

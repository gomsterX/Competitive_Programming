#Problem ID: MAX2
#Problem Name: Max power

n = int(input())
x = input()
x = x[::-1]
print(n - len(str(int(x))))

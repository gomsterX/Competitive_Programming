#Problem ID: URCALC
#Problem Name: Program Your Own CALCULATOR

a = int(input())
b = int(input())

c = input()

print(a+b) if c == '+' else print(a-b) if c == '-' else print(a*b) if c == '*' else print(a/b)

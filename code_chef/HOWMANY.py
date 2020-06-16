#Problem ID: HOWMANY
#Problem Name: HOW MANY DIGITS DO I HAVE

x = len(input())
if (x == 1 or x == 2 or x == 3):
    print(x)
else:
    print("More than 3 digits")

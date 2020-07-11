#Problem ID: TWEED
#Problem Name: Tweedle-Dee and Tweedle-Dum

for _ in range(int(input())):
    n, s = map(str, input().split())
    a = list(map(int, input().split()))

    if int(n) == 1 and  s == "Dee" and a[0] % 2 == 0:
        print("Dee")
    else:
        print("Dum")

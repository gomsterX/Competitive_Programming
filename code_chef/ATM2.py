#Problem ID: ATM2
#Problem Name: ATM Machine

for _ in range(int(input())):
    n, k = map(int, input().split())
    withdraw_money = list(map(int, input().split()))
    people = []
    for i in range(n):
        if (withdraw_money[i] <= k):
            k -= withdraw_money[i]
            people.append(1)
        else:
            people.append(0)
    print(''.join(map(str, people)))

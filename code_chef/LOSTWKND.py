#Problem ID: LOSTWKND
#Problem Name: Lost Weekends

for _ in range(int(input())):
    l = list(map(int, input().split()))
    c=0
    for i in range(5):
        c += l[-1]*l[i]
    if(c <= 24*5):
        print("No")
    else:
        print("Yes")


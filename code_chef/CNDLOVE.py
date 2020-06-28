#Problem ID: CNDLOVE
#Problem Name: Candy Love

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    if(sum(p) % 2 == 0):
        print("NO")
    else:
        print("YES")

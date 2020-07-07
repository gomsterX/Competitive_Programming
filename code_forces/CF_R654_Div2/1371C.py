#problem: contest/1371/problem/C
#problem Name:C. A Cookie for You

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if(a+b >= c+d and min(a, b) >= d):
        print("Yes")
    else:
        print("No")


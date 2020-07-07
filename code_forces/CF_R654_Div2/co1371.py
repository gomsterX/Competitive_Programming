#problem code: contest/1371/problem/A
#problem Name: Magical Sticks

for i in range(int(input())):
    n = int(input())
    n=n+1 if n%2!=0 else n
    print(int(n/2))

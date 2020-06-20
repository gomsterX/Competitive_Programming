#Problem ID: TALAZY
#Problem Name: Lazy Jem

for _ in range(int(input())):
    n, b, m = map(int, input().split())
    t_time = 0

    while(n>0):
        x = n//2 + n%2
        t_time += (b + (x * m))
        n -= x
        m *= 2

    print(t_time-b)

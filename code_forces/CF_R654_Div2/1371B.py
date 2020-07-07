#problem Name: B. Magical Calendar

for _ in range(int(input())):
    n, k = map(int, input().split())
    x = min(n, k)
    x = (((x-1)*x)//2)+1 if n<=k else (((x+1)*x)//2)
    print(x)

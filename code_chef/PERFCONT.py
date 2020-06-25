#Problem ID: PERFCONT
#Problem Name: A Balanced Contest

for _ in range(int(input())):
    n, p = map(int, input().split())
    x = list(map(int, input().split()))

    h = 0
    c = 0
    for i in range(n):
        if(x[i] <= p//10):
            h+=1
        elif(x[i] >= p//2):
            c +=1

    if(c==1 and h == 2):
        print("yes")
    else:
        print("no")


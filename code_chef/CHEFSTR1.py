#Problem ID: CHEFSTR1
#Problem Name: Chef and Strings

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    skp = 0
    for i in range(n-1):
        skp+= abs(l[i]-l[i+1])-1
    print(skp)


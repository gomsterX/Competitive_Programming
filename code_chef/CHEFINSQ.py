#Problem ID: CHEFINSQ
#Problem Name: Chef and Interesting Subsequences
fact = [1 for _ in range(51)]

for i in range(1,51):
    fact[i] = fact[i-1]*i

for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    arr = sorted(arr)
    n = arr.count(arr[k-1])
    r = arr[:k].count(arr[k-1])
    print(int(fact[n]/(fact[r]*fact[n-r])))



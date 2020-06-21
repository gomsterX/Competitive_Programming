#Problem ID: SIMPSTAT
#Problem Name: Simple Statistics

for _ in range(int(input())):
    n, k = map(int, input().split())
    j = list(map(int, input().split()))
    j.sort()
    j = j[k: n-k]
    print(sum(j)/len(j))

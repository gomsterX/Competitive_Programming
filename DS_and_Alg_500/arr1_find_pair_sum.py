#Problem ID: arr1_find_pair_sum
#Problem Name: Find pair with given sum in an array
#Complexity: O(Nlog(N))

def find_pair(l, s):
    l = sorted(l)
    x, y = 0, len(l)-1
    m = l[x] + l[y]
    while y>x:
        if m > s:
            y-=1
        elif s > m:
            x +=1
        else:
            print('pair found {} {}'.format(x, y))
            x+=1
        m = l[x]+l[y]

for _ in range(int(input())):
    l = list(map(int, input().split()))
    s = int(input())
    find_pair(l, s)

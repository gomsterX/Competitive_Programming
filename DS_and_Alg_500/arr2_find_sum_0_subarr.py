#Problem ID: arr2_find_sum_0_subarr
#Problem Name: check if array has zero sum subarray or not
#Complexity: O(N)

l = list(map(int, input().split()))
sums = []
s = 0
zero_sum_subarr = False
for i in l:
    s+=i
    if s in sums:
        zero_sum_subarr = True
        break
    sums.append(s)

if zero_sum_subarr:
    print('Exist')
else:
    print('No')


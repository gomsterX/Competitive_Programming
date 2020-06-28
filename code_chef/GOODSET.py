#Problem ID: GOODSET
#Problem Name: A Good Set

for _ in range(int(input())):
    n = int(input())
    for i in range(499, 499-n,-1):
        print(i," ",sep = '',  end='')

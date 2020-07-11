#Problem ID: DISCSHOP
#Problem Name: Discount in a Shop

for _ in range(int(input())):
    l = input()
    print(min([int(l[:i]+l[i+1:]) for i in range(len(l))]) )

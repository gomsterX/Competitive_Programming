#Problem ID: ZUBTRCNT
#Problem Name: D - Triangle Count

def count_triangle(l,k):
    a=0
    for i in range(l-k+1,0,-1):
        a+=i
    print("Case %d:"%j,a)
j=0
for _ in range(int(input())):
    j+=1
    l,k=map(int, input().split(" "))
    count_triangle(l,k)

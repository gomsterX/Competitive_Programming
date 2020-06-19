#Problem ID: SIMDISH
#Problem Name: Similar Dishes

for _ in range(int(input())):
    x = list(input().split())
    y = list(input().split())

    z = set(x + y)

    if(len(z) <= 6):
        print("similar")
    else:
        print("dissimilar")


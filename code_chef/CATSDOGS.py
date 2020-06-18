#Problem ID: CATSDOGS
#Problem Name: Cats and Dogs

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    max_legs = (x+y) * 4
    min_legs = max_legs - min(x, y*2) * 4

    if(z % 4 == 0 and z >= min_legs and z <= max_legs):
        print("yes")
    else:
        print("no")

#Problem ID: LIKECS01
#Problem Name: Subsequence Equality

for _ in range(int(input())):
    x = list(input())
    if(len(set(x)) < len(x)):
        print("yes")
    else:
        print("no")

#Problem ID: STRPALIN
#Problem Name: Palindromic substrings

for _ in range(int(input())):
    s1 = set(input())
    s2 = set(input())

    if(s1.intersection(s2)):
        print("Yes")
    else:
        print("No")



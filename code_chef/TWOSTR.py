#Problem ID: TWOSTR
#Problem Name: Chef and the Wildcard Matching

for _ in range(int(input())):
    s1 = input()
    s2 = input()

    no_match = False
    for i in range(len(s1)):
        if(s1[i] != '?' and s2[i] != '?' and (s1[i] != s2[i])):
            no_match = True

    if(no_match):
        print("No")
    else:
        print("Yes")


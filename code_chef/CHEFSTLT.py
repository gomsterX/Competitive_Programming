#Problem ID: CHEFSTLT
#Problem Name: Chef and Two Strings

for _ in range(int(input())):
    s1 = input()
    s2 = input()

    max_dif = 0
    min_dif = 0

    for i in range(len(s1)):
        if((s1[i] != s2[i]) or (s1[i] == '?' and s2[i] == '?')):
            max_dif += 1
        if((s1[i] != s2[i]) and (s1[i] != '?' and s2[i] != '?')):
            min_dif += 1

    print("{} {}".format(min_dif,  max_dif))


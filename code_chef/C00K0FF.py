#Problem ID: C00K0FF
#Problem Name: Chef and Cook-Off Contests

for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    if(("cakewalk" in l)and ( "simple" in l) and ("easy" in l)
            and (("easy-medium" in l)  or  ("medium" in l))
            and  (("medium-hard" in l) or  ("hard" in l))):
        print("Yes")
    else:
        print("No")

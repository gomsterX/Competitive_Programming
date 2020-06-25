#Problem ID: FRK
#Problem Name: Chef and Friends

frnds = 0
for _ in range(int(input())):
    s = input()
    if('ch' in s or 'he' in s or 'ef' in s):
        frnds += 1
print(frnds)


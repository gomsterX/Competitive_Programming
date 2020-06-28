#Problem ID: CODERLIF
#Problem Name: Coder Life Matters

for _ in range(int(input())):
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if i == 1:
            c+=1
        else:
            c = 0
        if(c>5):
            break
    if(c>5):
        print("#coderlifematters")
    else:
        print("#allcodersarefun")

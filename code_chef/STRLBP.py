#Problem ID: STRLBP
#Problem Name: Uniform Strings

for _ in range(int(input())):
    s = input()
    c = 0
    for i in range(len(s) - 1):
        if((s[i] == '1' and s[i+1] == '0')
                or (s[i] == '0' and s[i+1] == '1')):
            c+=1
            if(c >2):
                break
    if(c>2):
        print("non-uniform")
    else:
        print("uniform")

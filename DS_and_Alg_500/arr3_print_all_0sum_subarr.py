#problem Name: print all sub-arrays with zero sum

for _ in range(int(input('Number of test cases : '))):
    l = list(map(int, input('Array : ').split()))
    s = []
    x = 0
    for i in l:
        s.append(x)
        x += i
    s.append(x)

    ind = {}
    for i in range(len(s)):
        if str(s[i]) in ind:
            ind[str(s[i])].append(i)
        else:
            ind[str(s[i])] = [i]
    print(ind)
    for i in ind:
        x = ind[i]
        if len(x)>1:
            for i in range(len(x)):
                for j in range(i, len(x)):
                    if i != j:
                        print(l[x[i]:x[j]], ' ...........at...... ', x[i], x[j]-1)



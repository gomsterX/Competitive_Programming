#Problem ID: HRDSEQ
#Problem Name: Hard Sequence

for _ in range(int(input())):
    n=int(input())
    l=[0]
    for i in range(0,n-1):
        if l.count(l[-1])==1:
            l.append(0)
        else:
            for j  in range(len(l)-2,-1,-1):
                if l[j]==l[-1]:
                    break
            l.append(len(l)-1-j)

    print(l.count(l[-1]))

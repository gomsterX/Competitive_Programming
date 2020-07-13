#Problem ID: PROXYC
#Problem Name: Chef and Proxy

from math import ceil
for _ in range(int(input())):
    d = int(input())
    s = input()
    a = 0
    for i in range(2, d-2):
        if s[i] == 'A' and 'P' in s[i-2:i] and 'P' in s[i+1:i+3]:
            a += 1
    if(s.count('P') >= ceil(d*0.75)):
        print(0)
    elif(ceil(d*0.75) - s.count('P') <= a):
        print(ceil(d*0.75) - s.count('P'))
    else:
        print(-1)

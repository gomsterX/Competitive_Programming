#Problem ID: GOODBAD
#Problem Name: Good and Bad Persons

import re
for _ in range(int(input())):
    x, y = map(int, input().split())

    s = input()

    a = len(re.findall('[a-z]', s))
    b = len(re.findall('[A-Z]', s))

    if(b <= y and a > y):
        print("chef")
    elif(a <= y and b > y):
        print("brother")
    elif(b<=y and a <= y):
        print("both")
    else:
        print("none")

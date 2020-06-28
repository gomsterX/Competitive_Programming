#Problem ID: GIFTSRC
#Problem Name: Find Your Gift

for _ in range(int(input())):
    n = int(input())
    x, y = 0, 0
    s = list(input())
    i = 0
    while(i < n):
        if i+1 < len(s):
            if(s[i+1] == s[i] or (s[i] == 'L' and s[i+1] == 'R')
                    or(s[i] == 'R' and s[i+1] == 'L')
                    or(s[i] == 'U' and s[i+1] == 'D')
                    or(s[i] == 'D' and s[i+1] == 'U')):
                del(s[i+1])
                i -=1
        i+=1
    print(s.count('R') - s.count('L'), s.count('U') - s.count('D'))

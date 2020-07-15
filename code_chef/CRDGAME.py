#Problem ID: CRDGAME
#Problem Name: Chef and Card Game

for _ in range(int(input())):
    c = m = 0
    for i in range(int(input())):
        c_n, m_n = input().split()
        c_n, m_n = list(map(int, c_n)), list(map(int, m_n))
        if (sum(c_n) > sum(m_n)):
            c+=1
        elif sum(c_n) < sum(m_n):
            m +=1
        else:
            m+=1
            c+=1
    if c > m:
        print(0, c)
    elif c<m:
        print(1, m)
    else:
        print(2, c)

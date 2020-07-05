#Problem ID: CHEFWORK
#Problem Name: Workers

n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
mn_a = 100000
mn_t = 100000
mn_at = 1000000

for i in range(n):
    if(t[i] == 1 and c[i] < mn_t):
        mn_t = c[i]
    elif(t[i] == 2 and c[i] < mn_a):
        mn_a = c[i]
    elif(t[i] == 3 and c[i] < mn_at):
        mn_at = c[i]
print(min(mn_t+mn_a, mn_at))

#Problem ID: CHRL2
#Problem Name: Chef and String

x = input()
count = 0
c, h, e, f = 0, 0, 0, 0
for i in x:
    if i == 'C':
        c +=1
    elif i == 'H' and c > 0:
        c, h = c-1,h+1
    elif i == 'E' and h>0:
        h, e = h-1, e+1
    elif(e > 0):
        e, f = e-1, f+1
print(f)

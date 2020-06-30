#Problem ID: ACBALL
#Problem Name: Akhil And Colored Balls

for _ in range(int(input())):
    x = input()
    y = input()
    z = ''
    for i in range(len(x)):
        if(x[i] != y[i]):
            z+='B'
        else:
            if x[i] == 'B':
                z+='W'
            else:
                z+='B'
    print(z)

#Problem ID: ANKTRAIN
#Problem Name: Train Partner

for _ in range(int(input())):
    n = int(input())
    if(n%8 == 0):
        print(str(n-1) + 'SL')
    elif(n%7 == 0):
        print(str(n+1)+'SU')
    elif(n%6 == 0):
        print(str(n-3)+'UB')
    elif(n%5 == 0):
        print(str(n-3)+'MB')
    elif(n%4 == 0):
        print(str(n-3)+'LB')
    elif(n%3 == 0):
        print(str(n+3)+'UB')
    elif(n%2 == 0):
        print(str(n+3)+'MB')
    else:
        print(str(n+3)+'LB')

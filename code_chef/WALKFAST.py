#Problem ID: WALKFAST
#Problem Name: Train or Walk

for _ in range(int(input())):
    N,A,B,C,D,P,Q,Y=map(int,input().split())
    N=list(map(int,input().split()))
    walk=abs(N[B-1]-N[A-1])*P
    C_to_A=abs(N[C-1]-N[A-1])*P
    if(Y < C_to_A):
        print(walk)
    else:
        train= Y+abs((N[D-1]-N[C-1]))*Q+abs((N[D-1]-N[B-1]))*P
        print(min(walk,train))

#Problem ID: BFTT
#Problem Name: Balsa For The Three

for _ in range(int(input())):
    n = int(input())
    n+=1
    while True:
        if(str(n).count('3') >=3):
            break
        n+=1
    print(n)

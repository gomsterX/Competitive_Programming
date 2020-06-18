#Problem ID: CCOOK
#Problem Name: Chef and Cook-Off

for _ in range(int(input())):
    x = list(map(int, input().split()))
    x = sum(x)
    if(x >= 5):
        print("Jeff Dean")
    elif(x >= 4):
        print("Hacker")
    elif(x >= 3):
        print("Senior Developer")
    elif(x >= 2):
        print("Middle Developer")
    elif(x >= 1):
        print("Junior Developer")
    else:
        print("Beginner")


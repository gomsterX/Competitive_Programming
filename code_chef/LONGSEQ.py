#Problem ID: LONGSEQ
#Problem Name: Chef and digits of a number

for _ in range(int(input())):
    x = input()
    print("Yes") if(x.count('1') == 1 or x.count('0') == 1) else print("No")


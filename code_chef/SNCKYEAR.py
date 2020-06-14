#Problem ID: SNCKYEAR
#Problem Name: Chef and SnackDown

for _ in range(int(input())):
    x = [2010, 2015, 2016, 2017, 2019]
    if(int(input()) in x):
        print("HOSTED")
    else:
        print("NOT HOSTED")

#Problem ID: KTTABLE
#Problem Name: Kitchen Timetable

for _ in range(int(input())):
    x = int(input())
    avail_time = list(map(int, input().split()))
    req_time = list(map(int, input().split()))

    for i in range(x-1,0, -1):
        avail_time[i] -= avail_time[i-1]


    count = 0
    for i in range(x):
        if (req_time[i] <= avail_time[i]):
            count+=1

    print(count)

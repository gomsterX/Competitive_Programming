#Problem ID: FLOW015
#Problem Name: Gregorian Calendar

import datetime
for _ in range(int(input())):
    print(datetime.date(int(input()), 1, 1).strftime("%A").lower())

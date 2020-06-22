#Problem ID: CV
#Problem Name: CV

import re
for _ in range(int(input())):
    input()
    print(len(re.findall('[^aeiou][aeiou]', input())))

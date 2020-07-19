#Problem ID: find_all_0sum_subarr
#Problem Name: print all sub arrays with zero sum

for _ in range(int(input('Number of test cases : '))):
    l = list(map(int, input('Enter array : ').split()))
    l_pointer = 0
    r_pointer = 0
    s = l[0]
    for i in range(len(l)):
        if s == 0:
            print(l_pointer, r_pointer)
            s = l[r_pointer]
            l_pointer = r_pointer
            r_pointer += 1
        else:
            if s > 0:
                r_pointer += 1
                s += l[r_pointer]
            else:
                s -= l[l_pointer]
                l_pointer += 1



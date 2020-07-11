#Problem ID: USANBOLT
#Problem Name: Usain Bolt vs Tiger

from math import sqrt
for _ in range(int(input())):
    fnsh_dist, dist_to_blt, tig_acc, blt_spd = map(int, input().split())
    tig_fnsh_dist = dist_to_blt + fnsh_dist
    bolt_time_to_finish = fnsh_dist/blt_spd
    tiger_time_to_finish = sqrt((2*tig_fnsh_dist)/tig_acc)

    if bolt_time_to_finish < tiger_time_to_finish:
        print("Bolt")
    else:
        print("Tiger")

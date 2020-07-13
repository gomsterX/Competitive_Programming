#Problem ID: TYPING
#Problem Name: Chef and Typing

for _ in range(int(input())):
    t = 0
    words = []
    for m in range(int(input())):
        xt = 0
        x = input()
        fhand = True
        f_hand = True if x[0] == 'd' or x[0] == 'f' else False
        for i in x:
            if i == 'd' or i == 'f':
                if f_hand:
                    f_hand = False
                    xt += 2
                else:
                    xt +=4
            elif i == 'j' or i == 'k':
                if not f_hand:
                    f_hand = True
                    xt +=2
                else:
                    xt += 4
        if x in words:
            xt = xt/2
        else:
            words.append(x)
        t += xt
    print(int(t))
